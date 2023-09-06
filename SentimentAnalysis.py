import tkinter as tk
import boto3
root=tk.Tk()
root.geometry("500x500")
root.title("Sentiment Analyzer")
root.configure(background="light blue", bd="5")
textbox=tk.Text(root, height=25)
textbox.pack()
def func():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x300")
    newWindow.title("Sentiment Analysis")
    aws_mag_con=boto3.session.Session(profile_name="SentimentAnalyzer")
    client=aws_mag_con.client(service_name='comprehend',region_name="us-east-1")
    result = "Entered Text : " + textbox.get("1.0","end") + "\n"
    response = client.detect_sentiment(Text=result,LanguageCode='en')
    tk.Label(newWindow, text = "\nThe prominant Sentiment is " + response['Sentiment'] + "\n\n", font='Helvetica 15 bold').pack()
    tk.Label(newWindow, text = "The Sentiment Score is " + "\n", font='Helvetica 12 bold').pack()
    p = str(response['SentimentScore']['Positive'])
    n = str(response['SentimentScore']['Negative'])
    nu = str(response['SentimentScore']['Neutral'])
    m = str(response['SentimentScore']['Mixed'])
    tk.Label(newWindow, text = "Positive : " + p + "\n", font='Helvetica 8').pack()
    tk.Label(newWindow, text = "Negative : " + n + "\n", font='Helvetica 8').pack()
    tk.Label(newWindow, text = "Neutral : " + nu + "\n", font='Helvetica 8').pack()
    tk.Label(newWindow, text = "Mixed : " + m + "\n", font='Helvetica 8').pack()
btn=tk.Button (root, height=1,width=10, text="Analyze", command=func)
btn.pack()
root.mainloop()