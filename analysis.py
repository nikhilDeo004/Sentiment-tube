import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def pie_chart(df):
    """
    Generate a pie chart to visualize sentiment distribution.
    """
    sentiment_counts = df.groupby(['label']).size()
    
    # ✅ CHANGED: Created figure and axis explicitly
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    
    # ✅ CHANGED: Use ax with pie plot instead of global plt
    sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12)
    ax.set_ylabel("")  # Optional: hides y-label

    # ✅ CHANGED: Pass figure to st.pyplot()
    st.pyplot(fig)

def positive_wordcloud(merged_df):
    """
    Generate a word cloud for positive comments.
    """
    positive_comments = merged_df['Comment'][merged_df["label"] == 'POS']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    
    # ✅ CHANGED: Separated wordcloud generation and figure plotting
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words)
    wc_generated = wc.generate(str(positive_comments))

    # ✅ CHANGED: Created figure and axis explicitly
    fig, ax = plt.subplots()
    ax.imshow(wc_generated, interpolation="bilinear")
    ax.set_title("Positive comments - Wordcloud")
    ax.axis("off")

    # ✅ CHANGED: Pass figure to st.pyplot()
    st.pyplot(fig)

def negative_wordcloud(merged_df):
    """
    Generate a word cloud for negative comments.
    """
    negative_comments = merged_df['Comment'][merged_df["label"] == 'NEG']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    
    # ✅ CHANGED: Separated wordcloud generation and figure plotting
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words)
    wc_generated = wc.generate(str(negative_comments))

    # ✅ CHANGED: Created figure and axis explicitly
    fig, ax = plt.subplots()
    ax.imshow(wc_generated, interpolation="bilinear")
    ax.set_title("Negative comments - Wordcloud")
    ax.axis("off")

    # ✅ CHANGED: Pass figure to st.pyplot()
    st.pyplot(fig)

def neutral_wordcloud(merged_df):
    """
    Generate a word cloud for neutral comments.
    """
    neutral_comments = merged_df['Comment'][merged_df["label"] == 'NEU']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)

    # ✅ CHANGED: Separated wordcloud generation and figure plotting
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=stop_words)
    wc_generated = wc.generate(str(neutral_comments))

    # ✅ CHANGED: Created figure and axis explicitly
    fig, ax = plt.subplots()
    ax.imshow(wc_generated, interpolation="bilinear")
    ax.set_title("Neutral comments - Wordcloud")
    ax.axis("off")

    # ✅ CHANGED: Pass figure to st.pyplot()
    st.pyplot(fig)
