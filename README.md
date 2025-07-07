# 🪙 Gold Rate Chatbot (AWS Lambda + Amazon Lex)

This project is an **Amazon Lex chatbot** that provides real-time gold rates for Hyderabad. It uses **AWS Lambda** with Python to scrape gold prices from [BankBazaar](https://www.bankbazaar.com/gold-rate.html) and respond to user queries like:  

- 🗨️ *“What is the gold rate today?”*  
- 🗨️ *“Gold price in Hyderabad?”*  

The chatbot fetches the latest 24K gold rate and gives users an instant reply.

---

## 🚀 How it Works

1. 📝 **Web Scraping**:  
   The Lambda function scrapes the **24K gold rate** for Hyderabad from [BankBazaar](https://www.bankbazaar.com/gold-rate.html) using `requests` and `BeautifulSoup`.  

2. 🤖 **Amazon Lex Chatbot**:  
   The Lex bot is trained to understand gold rate queries. It triggers the Lambda function whenever a user asks about gold prices.

3. 💬 **Response**:  
   The bot replies with the current gold rate in Hyderabad or an error message if the rate isn’t available.

---

## 📂 Project Structure

gold-rate-lex-chatbot/
│
├── lambda_function.py # Python code for AWS Lambda
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🛠️ Deployment Steps

### 🖥️ 1. Deploy Lambda Function
- Go to [AWS Lambda Console](https://console.aws.amazon.com/lambda/).  
- Create a new Lambda function (Python 3.x runtime).  
- Upload `lambda_function.py` or paste its code.  
- Add a **layer** for external libraries (`requests`, `beautifulsoup4`) or include them in a deployment package.  
- Set the handler to `lambda_function.lambda_handler`.

---

### 💬 2. Create Amazon Lex Bot
- Go to [Amazon Lex Console](https://console.aws.amazon.com/lex/).  
- Create a new bot (V2 preferred).  
- Add an **intent** (e.g., `GetGoldRate`) and sample utterances like:  
  - *“What’s the gold rate in Hyderabad?”*  
  - *“Gold price today?”*  
- Configure the intent to call your Lambda function.

---

### 🧪 3. Test
- Use the **Lex test window** to ask:  
  > *“Gold rate Hyderabad today”*  
- The bot will respond with the current 24K gold price.

---

## 📦 Requirements

- Python 3.x  
- AWS Lambda  
- Amazon Lex (V2)  
- Libraries:
  - `requests`
  - `beautifulsoup4`

