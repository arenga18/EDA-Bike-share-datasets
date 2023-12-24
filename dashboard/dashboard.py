import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st

df_day = pd.read_csv('cleaned_df_day.csv')
df_hour = pd.read_csv('cleaned_df_hour.csv')

df_day.reset_index(inplace = True)
df_hour.reset_index(inplace = True)

weekday_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
season_order = ['Spring','Summer', 'Fall','Winter']
df_day['season'] = pd.Categorical(df_day['season'], categories=season_order, ordered=True)
df_day['month'] = pd.Categorical(df_day['month'], categories=month_order, ordered=True)
df_day['weekday'] = pd.Categorical(df_day['weekday'], categories=weekday_order, ordered=True)
custom_palette = sns.color_palette(['#e60000', '#1919ff'])

st.header('Dashboard Bike Sharing Dataset')

st.subheader('Hari, dan jam tersibuk untuk bike sharing berdasarkan tahun')
year_tab1, year_tab2 = st.tabs(["Hari", "Jam"])
with year_tab1:
    with st.container():
        fig = plt.figure(figsize = (10, 5))
        sns.barplot(x = 'weekday', y = 'count', data = df_day, hue = 'year', palette=custom_palette, errorbar=None)
        plt.title('Jumlah pengguna bike sharing berdasarkan hari dan tahun')
        plt.xlabel('Days')
        plt.ylabel('Count')
        st.pyplot(fig) 
    with st.expander("See explanation"):
        st.write(
            """Hari Kamis menunjukan puncak penggunaan bike sharing pada 2012, sementara pada tahun 2011, penggunaan bike sharing pada hari Senin, Selasa, dan Jumat cukup seimbang, dengan jumlah yang kurang lebih sama.
            """
        )
    
with year_tab2:
    with st.container():
        fig = plt.figure(figsize = (10, 5))
        sns.barplot(x = 'hour', y = 'count', data = df_hour, hue = 'year',palette=custom_palette, errorbar=None)
        plt.title('Jumlah pengguna bike sharing berdasarkan jam dan tahun')
        plt.xlabel('Hour')
        plt.ylabel('Count')
        plt.show()
        st.pyplot(fig)
    with st.expander("See explanation"):
        st.write(
            """Jam 17:00 menunjukan puncak penggunaan bike sharing pada tahun 2011 dan 2012
            """
        )

st.subheader('Perfoma penggunaan bike sharing dalam beberapa tahun terakhir')
df_2012 = df_day[df_day['year'] == 2012]
df_2011 = df_day[df_day['year'] == 2011]

monthly_df_2012 = df_2012.groupby(by='month').agg({
    "count": "sum"
})
monthly_df_2011 = df_2011.groupby(by='month').agg({
    "count": "sum"
})
monthly_df_2012 = monthly_df_2012.reset_index()
monthly_df_2011 = monthly_df_2011.reset_index()

fig = plt.figure(figsize=(14, 7))
plt.plot(monthly_df_2012['month'], monthly_df_2012['count'], label="2012", marker=".",color='#e60000', linewidth=2)
plt.plot(monthly_df_2011['month'], monthly_df_2011['count'], label="2011", marker=".",color= '#1919ff', linewidth=2)
plt.legend() 
st.pyplot(fig)

with st.expander("See explanation"):
        st.write(
            """
            - Penggunaan bike sharing pada 2011 mengalami peningkatan cukup pesat sejak awal bulan Januari sampai bulan Juni, lalu mengalami penurunan hingga bulan Desember
            - Penggunaan bike sharing pada 2012 mengalami peningkatan sejak awal bulan Januari sampai dengan September, dan mengalami penurunan hingga bulan Desember
            """
        )

st.subheader('Perfoma penggunaan bike sharing dalam beberapa tahun terakhir')
colors_ = [ '#d1d1ff',  '#d1d1ff',"#1919ff", "#d1d1ff",]
fig = plt.figure(figsize = (10, 5))
sns.barplot(x = 'season', y = 'count', data = df_day.sort_values(by='season', ascending=False), palette=colors_,  errorbar=None)
plt.title('Jumlah pengguna bike sharing berdasarkan musim')
plt.xlabel('Season')
plt.ylabel('Count')
st.pyplot(fig)

with st.expander("See explanation"):
        st.write(
            """Musim gugur menunjukan pengguna bike share terbanyak.
            """
        )

