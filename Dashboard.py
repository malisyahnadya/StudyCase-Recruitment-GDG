import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Proyek Analisis Data E-Commerce')
st.markdown("Oleh: **Malisyah Nadya Marvini**")

df = pd.read_csv('data_ecommerce.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

st.header("1. Analisis Persebaran Pelanggan")
st.subheader("Kota mana yang memiliki jumlah customers terbanyak?")

city_counts = df.groupby('customer_city')['customer_unique_id'].nunique().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(city_counts.index, city_counts.values, color='#1f77b4')
ax.set_title("10 Kota dengan Jumlah Customer Terbanyak")
ax.set_xlabel("Nama Kota")
ax.set_ylabel("Jumlah Customer Unik")
plt.xticks(rotation=45)

st.pyplot(fig)

with st.expander("Lihat Insight"):
    st.write("Berdasarkan grafik di atas, \n- Kota yang memiliki customer terbanyak adalah São Paulo yang sangat mendoninasi di bandingkan kota lainnya \n- Distribusi customer menunjukkan bahwa jumlah customer tidak merata antar kota. Terdapat kota yang mendominasi jumlah customer.\n- terbesar karena memiliki kontribusi transaksi yang signifikan.")

st.header("2. Analisis Kategori Produk")
st.subheader("Kategori produk apa yang paling banyak terjual dan menghasilkan pendapatan tertinggi?")

category_counts = df['product_category_name'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(category_counts.index, category_counts.values, color='#1f77b4')
ax.set_title("10 Kategori Produk Terlaris")
ax.set_xlabel("Kategori Produk")
ax.set_ylabel("Jumlah Produk Terjual")
plt.xticks(rotation=45)

st.pyplot(fig)

category_revenue = df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)

fig_rev, ax_rev = plt.subplots(figsize=(10, 6))
ax_rev.bar(category_revenue.index, category_revenue.values, color='#1f77b4') 
ax_rev.set_title("10 Kategori Produk dengan Pendapatan Tertinggi")
ax_rev.set_xlabel("Kategori Produk")
ax_rev.set_ylabel("Total Pendapatan")
plt.xticks(rotation=45)

st.pyplot(fig_rev)

with st.expander("Lihat Insight"):
    st.write("Dari Grafik diatas: \n- Kategori produk yang banyak terjual adalah cama_mesa_banho sedangkan yang menghasilkan pendapatan tertinggi adalah beleza_saude \n- Tidak semua kategori dengan jumlah transaksi tinggi menghasilkan pendapatan tertinggi. Terdapat kategori yang sering dibeli dengan harga relatif rendah dan jarang dibeli tetapi berkontribusi besar pada revenue \n- strategi bisnis perlu disesuaikan berdasarkan produk berorientasi volume dan produk berorientasi pendapatan")

st.divider()
st.caption("Copyright © Malisyah Nadya Marvini 2025")