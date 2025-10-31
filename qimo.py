import pandas as pd
import plotly.express as px

if page == "专业数据分析":
    st.title("专业数据分析")
    st.divider()

   

    def load_data():
        df = pd.read_csv("student_data_adjusted_rounded.csv")
        return df
    
    df = load_data()
    st.dataframe(df.head())  # 展示数据前几行

    st.divider()


    st.subheader("1. 各专业成绩分布对比")
    fig1 = px.histogram(
        df, 
        x="专业", 
        y="成绩", 
        color="性别", 
        barmode="group", 
        title="各专业成绩分布"
    )
    st.plotly_chart(fig1, use_container_width=True)


    st.subheader("2. 各专业学习趋势对比")
    fig2 = px.line(
        df, 
        x="学期", 
        y="学习时长", 
        color="专业", 
        title="各专业学习时长趋势"
    )
    st.plotly_chart(fig2, use_container_width=True)


    st.subheader("3. 各专业出勤率分析")
    attendance = df.groupby("专业")["出勤率"].mean().reset_index()
    fig3 = px.pie(
        attendance, 
        names="专业", 
        values="出勤率", 
        title="各专业平均出勤率"
    )
    st.plotly_chart(fig3, use_container_width=True)
