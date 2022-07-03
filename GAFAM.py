import yfinance as yf
import streamlit as st

st.title("GAFAM stocks prices app")

# Google
with st.container():
    st.write("""--------""")
    st.write("""## Google""")
    google_tickerSymbol = 'GOOGL'
    google_tickerData = yf.Ticker(google_tickerSymbol)
    google_tickerDf = google_tickerData.history(period='1m', start='2005-1-1', end='2022-7-1')

    st.write("""### Open """)
    st.line_chart(google_tickerDf.Open)
    st.write("""### Close""")
    st.line_chart(google_tickerDf.Close)
    st.write("""### Volume""")
    st.line_chart(google_tickerDf.Volume)
    st.write("""### High""")
    st.line_chart(google_tickerDf.High)
    st.write("""### Low""")
    st.line_chart(google_tickerDf.Low)

# Apple
with st.container():
    st.write("""--------""")
    st.write("""## Apple""")
    apple_tickerSymbol = 'AAPL'
    apple_tickerData = yf.Ticker(apple_tickerSymbol)
    apple_tickerDf = apple_tickerData.history(period='1m', start='2005-1-1', end='2022-7-1')

    st.write("""### Open """)
    st.line_chart(apple_tickerDf.Open)
    st.write("""### Close""")
    st.line_chart(apple_tickerDf.Close)
    st.write("""### Volume""")
    st.line_chart(apple_tickerDf.Volume)
    st.write("""### High""")
    st.line_chart(apple_tickerDf.High)
    st.write("""### Low""")
    st.line_chart(apple_tickerDf.Low)

# Facebook
with st.container():
    st.write("""--------""")
    st.write("""## Facebook""")
    fb_tickerSymbol = 'FB-USD'
    fb_tickerData = yf.Ticker(fb_tickerSymbol)
    fb_tickerDf = fb_tickerData.history(period='1m', start='2005-1-1', end='2022-7-1')

    st.write("""### Open """)
    st.line_chart(fb_tickerDf.Open)
    st.write("""### Close""")
    st.line_chart(fb_tickerDf.Close)
    st.write("""### Volume""")
    st.line_chart(fb_tickerDf.Volume)
    st.write("""### High""")
    st.line_chart(fb_tickerDf.High)
    st.write("""### Low""")
    st.line_chart(fb_tickerDf.Low)

# Amazon
with st.container():
    st.write("""--------""")
    st.write("""## Amazon""")
    amazon_tickerSymbol = 'AMZN'
    amazon_tickerData = yf.Ticker(amazon_tickerSymbol)
    amazon_tickerDf = amazon_tickerData.history(period='1m', start='2005-1-1', end='2022-7-1')

    st.write("""### Open """)
    st.line_chart(amazon_tickerDf.Open)
    st.write("""### Close""")
    st.line_chart(amazon_tickerDf.Close)
    st.write("""### Volume""")
    st.line_chart(amazon_tickerDf.Volume)
    st.write("""### High""")
    st.line_chart(amazon_tickerDf.High)
    st.write("""### Low""")
    st.line_chart(amazon_tickerDf.Low)

# Microsoft
with st.container():
    st.write("""--------""")
    st.write("""## Microsoft""")
    msft_tickerSymbol = 'MSFT'
    msft_tickerData = yf.Ticker(msft_tickerSymbol)
    msft_tickerDf = msft_tickerData.history(period='1m', start='2005-1-1', end='2022-7-1')

    st.write("""### Open """)
    st.line_chart(msft_tickerDf.Open)
    st.write("""### Close""")
    st.line_chart(msft_tickerDf.Close)
    st.write("""### Volume""")
    st.line_chart(msft_tickerDf.Volume)
    st.write("""### High""")
    st.line_chart(msft_tickerDf.High)
    st.write("""### Low""")
    st.line_chart(msft_tickerDf.Low)


