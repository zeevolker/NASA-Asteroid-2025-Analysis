import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="NASA Asteroid Dashboard",
    page_icon="☄️",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    df = pd.read_csv("data/asteroids_2025.csv")
    return df

df = load_data()

# =========================
# TITLE
# =========================

st.title("☄️ NASA Near-Earth Asteroid Analysis 2025")

st.markdown(
    """
    Interactive dashboard built from NASA NeoWs API data by Zee.
    """
)

# Sidebar
st.sidebar.title(
    "☄️ NASA Dashboard"
)

search = st.sidebar.text_input(
    "Search Asteroid"
)

selected_months = st.sidebar.multiselect(
    "Month",
    sorted(df["month"].unique()),
    default=sorted(df["month"].unique())
)

selected_size = st.sidebar.multiselect(
    "Size Category",
    sorted(df["size_category"].unique()),
    default=sorted(df["size_category"].unique())
)

filtered_df = df[
    (df["month"].isin(selected_months))
    &
    (df["size_category"].isin(selected_size))
]

if search:

    filtered_df = filtered_df[
        filtered_df["name"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# KPI Cards
col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(
        "Total",
        len(filtered_df)
    )

with col2:

    st.metric(
        "Hazardous",
        int(
            filtered_df["hazardous"]
            .sum()
        )
    )

with col3:

    st.metric(
        "Avg Velocity",
        f"{filtered_df['velocity_kmh'].mean():,.0f}"
    )

with col4:

    st.metric(
        "Closest",
        f"{filtered_df['miss_distance_ld'].min():.2f} LD"
    )

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Distribution",
    "Top Rankings",
    "Risk Analysis",
    "Dataset"
])

# Tab 1: Overview
with tab1:

    st.header(
        "Executive Summary"
    )
    total = len(filtered_df)

    hazardous = int(
        filtered_df["hazardous"]
        .sum()
    )

    rate = (
        hazardous / total * 100
    )
    st.info(
        f"""
        Total Asteroids: {total:,}

        Hazardous: {hazardous:,}

        Hazardous Rate:
        {rate:.2f}%
        """
    )

# Automated Insights
    st.subheader(
        "Automated Insights"
    )
    
    largest_name = (
        filtered_df.loc[
            filtered_df[
                "diameter_avg_m"
            ].idxmax(),
            "name"
        ]
    )

    fastest_name = (
        filtered_df.loc[
            filtered_df[
                "velocity_kmh"
            ].idxmax(),
            "name"
        ]
    )

    closest_name = (
        filtered_df.loc[
            filtered_df[
                "miss_distance_ld"
            ].idxmin(),
            "name"
        ]
    )
    
    st.success(
            f"""
    Largest:
    {largest_name}

    Fastest:
    {fastest_name}

    Closest:
    {closest_name}
    """
        )

# Asteroid Details
    st.subheader(
            "Asteroid Detail"
        )

    selected = st.selectbox(
            "Select Asteroid",
            filtered_df["name"]
            .unique()
    )

    asteroid = filtered_df[
            filtered_df["name"]
            == selected
        ].iloc[0]

# Details Matrix
    col1,col2 = st.columns(2)

    with col1:

            st.metric(
                "Diameter",
                f"{asteroid['diameter_avg_m']:.2f} m"
            )

            st.metric(
                "Velocity",
                f"{asteroid['velocity_kmh']:,.0f} km/h"
            )

    with col2:

            st.metric(
                "Distance",
                f"{asteroid['miss_distance_ld']:.2f} LD"
            )

            st.metric(
                "Risk Score",
                f"{asteroid['risk_score']:.4f}"
            )

# Risk Level Indicator
    risk = asteroid["risk_score"]

    if risk < 1:

            st.success(
                "🟢 LOW RISK"
            )

    elif risk < 5:

            st.warning(
                "🟡 MEDIUM RISK"
            )

    else:

            st.error(
                "🔴 HIGH RISK"
            )
        
# NASA Link
    st.markdown(
            f"""
            [NASA JPL Detail]
            ({asteroid['nasa_jpl_url']})
            """
        )

# Hazardous Distribution
    fig = px.pie(
            filtered_df,
            names="hazardous"
        )

    st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Asteroid per Month
    monthly = (
            filtered_df
            .groupby("month")
            .size()
            .reset_index(
                name="count"
            )
        )

    fig = px.line(
            monthly,
            x="month",
            y="count"
        )

    st.plotly_chart(
            fig,
            use_container_width=True
        ) 

# =====================================================
# DISTRIBUTION ANALYSIS
# =====================================================

with tab2:

    st.header("Distribution Analysis")

    # Diameter Distribution
    st.subheader("Diameter Distribution")

    fig = px.histogram(
        filtered_df,
        x="diameter_avg_m",
        nbins=50,
        title="Diameter Distribution (Meters)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Velocity Distribution
    st.subheader("Velocity Distribution")

    fig = px.histogram(
        filtered_df,
        x="velocity_kmh",
        nbins=50,
        title="Velocity Distribution (km/h)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Miss Distance Distribution
    st.subheader("Miss Distance Distribution")

    fig = px.histogram(
        filtered_df,
        x="miss_distance_ld",
        nbins=50,
        title="Miss Distance Distribution (Lunar Distance)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Size Category
    st.subheader("Size Category Distribution")

    size_count = (
        filtered_df["size_category"]
        .value_counts()
        .reset_index()
    )

    size_count.columns = [
        "size_category",
        "count"
    ]

    fig = px.bar(
        size_count,
        x="size_category",
        y="count",
        color="size_category",
        title="Asteroid Size Categories"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
# =====================================================
# TOP RANKINGS
# =====================================================

with tab3:

    st.header("Top Rankings")

    # Largest
    st.subheader("Top 10 Largest Asteroids")

    top_biggest = (
        filtered_df
        .nlargest(
            10,
            "diameter_avg_m"
        )
    )

    fig = px.bar(
        top_biggest,
        x="diameter_avg_m",
        y="name",
        orientation="h",
        title="Largest Asteroids"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Fastest
    st.subheader("Top 10 Fastest Asteroids")

    top_fastest = (
        filtered_df
        .nlargest(
            10,
            "velocity_kmh"
        )
    )

    fig = px.bar(
        top_fastest,
        x="velocity_kmh",
        y="name",
        orientation="h",
        title="Fastest Asteroids"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Closest
    st.subheader("Top 10 Closest Asteroids")

    top_closest = (
        filtered_df
        .nsmallest(
            10,
            "miss_distance_ld"
        )
    )

    fig = px.bar(
        top_closest,
        x="miss_distance_ld",
        y="name",
        orientation="h",
        title="Closest Approaches"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Risk Score
    st.subheader("Top 10 Highest Risk Score")

    top_risk = (
        filtered_df
        .nlargest(
            10,
            "risk_score"
        )
    )

    fig = px.bar(
        top_risk,
        x="risk_score",
        y="name",
        orientation="h",
        color="risk_score",
        title="Highest Risk Asteroids"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
# =====================================================
# RISK ANALYSIS
# =====================================================

with tab4:

    st.header("Risk Analysis")

    # Scatter Plot
    st.subheader("Diameter vs Velocity")

    fig = px.scatter(
        filtered_df,
        x="diameter_avg_m",
        y="velocity_kmh",
        color="hazardous",
        hover_name="name",
        size="risk_score",
        title="Diameter vs Velocity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Correlation Matrix
    st.subheader("Correlation Matrix")

    corr_cols = [
        "diameter_avg_m",
        "velocity_kmh",
        "miss_distance_km",
        "risk_score",
        "impact_energy"
    ]

    corr = (
        filtered_df[corr_cols]
        .corr()
        .round(2)
    )

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.values.astype(str),
        showscale=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Hazardous Table
    st.subheader(
        "Potentially Hazardous Asteroids"
    )

    hazard_df = filtered_df[
        filtered_df["hazardous"]
        == True
    ]

    st.dataframe(
        hazard_df[
            [
                "name",
                "diameter_avg_m",
                "velocity_kmh",
                "miss_distance_ld",
                "risk_score"
            ]
        ],
        use_container_width=True
    )

    # Risk Distribution
    st.subheader("Risk Score Distribution")

    fig = px.histogram(
        filtered_df,
        x="risk_score",
        nbins=50,
        title="Risk Score Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
# =====================================================
# DATASET EXPLORER
# =====================================================

with tab5:

    st.header("Dataset Explorer")

    st.subheader(
        "Filtered Dataset"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.subheader(
        "Summary Statistics"
    )

    st.dataframe(
        filtered_df.describe(),
        use_container_width=True
    )

    st.subheader(
        "Dataset Information"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Rows",
            filtered_df.shape[0]
        )

    with col2:

        st.metric(
            "Columns",
            filtered_df.shape[1]
        )

    with col3:

        st.metric(
            "Hazardous",
            int(
                filtered_df["hazardous"]
                .sum()
            )
        )

    # Download CSV

    csv = filtered_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download Filtered Dataset",
        data=csv,
        file_name="asteroids_filtered.csv",
        mime="text/csv"
    )
    
st.divider()

st.caption(
    """
    NASA Near-Earth Asteroid Dashboard
    | Data Source: NASA NeoWs API
    | Built with Python, Pandas, Plotly & Streamlit
    """
)