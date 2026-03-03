"""
charts.py — Plotly chart builders for the SecureScan AI dashboard.
Each function returns a Plotly figure ready to display.
"""

import plotly.graph_objects as go


def create_risk_gauge(score, level):
    """Create a gauge chart showing the overall risk score (0-100)."""
    if score >= 75:
        bar_color = "#ff4757"
    elif score >= 50:
        bar_color = "#ffa502"
    elif score >= 25:
        bar_color = "#00d4ff"
    else:
        bar_color = "#00ff88"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"font": {"size": 52, "color": "#e6edf3", "family": "JetBrains Mono"}},
        title={"text": f"RISK LEVEL: {level}", "font": {"size": 14, "color": "#8b949e"}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#21262d", "dtick": 25,
                     "tickfont": {"color": "#484f58", "size": 10}},
            "bar": {"color": bar_color, "thickness": 0.7},
            "bgcolor": "#161b22",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 25], "color": "rgba(0, 255, 136, 0.08)"},
                {"range": [25, 50], "color": "rgba(0, 212, 255, 0.08)"},
                {"range": [50, 75], "color": "rgba(255, 165, 2, 0.08)"},
                {"range": [75, 100], "color": "rgba(255, 71, 87, 0.08)"},
            ],
            "threshold": {"line": {"color": bar_color, "width": 3}, "thickness": 0.8, "value": score},
        },
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=260, margin=dict(l=30, r=30, t=60, b=20),
    )
    return fig


def create_severity_donut(severity_counts):
    """Create a donut chart breaking down findings by severity level."""
    labels, values, colors = [], [], []
    color_map = {"Critical": "#ff4757", "High": "#ffa502", "Medium": "#00d4ff", "Low": "#00ff88"}

    for sev in ["Critical", "High", "Medium", "Low"]:
        if severity_counts.get(sev, 0) > 0:
            labels.append(sev)
            values.append(severity_counts[sev])
            colors.append(color_map[sev])

    fig = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=0.65,
        marker=dict(colors=colors, line=dict(color="#0d1117", width=2)),
        textinfo="label+value",
        textfont=dict(size=11, color="#e6edf3", family="Inter"),
    )])
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=280, margin=dict(l=20, r=20, t=30, b=20), showlegend=False,
        annotations=[dict(text="SEVERITY", x=0.5, y=0.5, font_size=11,
                          font_color="#8b949e", showarrow=False)],
    )
    return fig


def create_category_bar(category_counts):
    """Create a horizontal bar chart showing findings by category."""
    sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    categories = [c[0] for c in sorted_cats]
    counts = [c[1] for c in sorted_cats]

    cat_colors = {
        "Credentials": "#ff4757", "PII": "#ffa502", "Financial": "#7b61ff",
        "Network": "#00d4ff", "Code Vulnerability": "#ff6b81",
    }
    colors = [cat_colors.get(c, "#00ff88") for c in categories]

    fig = go.Figure(data=[go.Bar(
        x=counts, y=categories, orientation='h',
        marker=dict(color=colors, line=dict(width=0)),
        text=counts, textposition='outside',
        textfont=dict(color="#e6edf3", size=12, family="JetBrains Mono"),
    )])
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=max(180, len(categories) * 50 + 60),
        margin=dict(l=10, r=40, t=20, b=20),
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(tickfont=dict(color="#b0bec5", size=12, family="Inter"), autorange="reversed"),
        bargap=0.35,
    )
    return fig
