# Web Scraping Using Python  

## 📌 Project Overview  
This project demonstrates how to perform **web scraping** using Python in a crisp and efficient manner. We have used multiple Python libraries, such as:  
- `BeautifulSoup` – to parse HTML and extract data  
- `lxml` – for fast HTML parsing  
- `requests` – to send HTTP requests  
- `time` – to add delays and avoid getting blocked  

---

## 🚀 Hookup Story  
One day, a client named **Rohit** approached us. He had started a **tour and travel business** and wanted detailed information about various hotels, including:  
✔️ Price  
✔️ Social Reviews  
✔️ Availability  
✔️ Contact Details  

Our task was to **analyze the hotels** and sort them based on the client’s requirements. This data would help Rohit **negotiate deals** with hotels and decide on the commission structure.  

To gather this information, we targeted one of the most popular hotel booking platforms — **Booking.com** — to scrape data effectively.  

---

## 🛠️ Tech Stack  
- **Python** – Core programming language  
- **BeautifulSoup** – For HTML parsing  
- **lxml** – For fast and efficient parsing  
- **Requests** – To make HTTP requests  
- **CSV** – To store scraped data  
- **Time & Random** – To handle delays and avoid IP blocking  

---

## 📂 Project Structure  
├── main.py  
├── requirements.txt  
├── README.md  
└── output/  
      &emsp; └── scraped_data.csv

---

## 🏃‍♂️ How to Run the Project
### 1. Clone the repository
git clone https://github.com/yourusername/web-scraping-python.git

### 2. Navigate to the project directory
cd web-scraping-python

### 3. Create a virtual environment (Optional)
python -m venv venv
source venv/bin/activate    # On Linux/MacOS
venv\Scripts\activate       # On Windows

### 4. Install the dependencies
pip install -r requirements.txt

### 5. Run the script
python main.py

---

## 🔍 Example Usage
url = 'https://www.booking.com/hotels'
file_name = 'scraped_data.csv'
scrape_data(url, file_name)

---

## 📊 Sample Output
| **Hotel Name** | **Location** | **Price** | **Review** | **Rating** | **Contact Link** |
|---|---|---|---|---|---| 
| Hotel ABC	 | Delhi | ₹2940 | 25 | 8.9 | link |
| Hotel XYZ	 | Mumbai | ₹3100 | 19 | 9.1 | link |

---

## ✅ Features
✔️ Fast and Efficient Scraping  
✔️ Handles Large Data with Ease  
✔️ Saves Data in CSV Format  
✔️ Customizable Input and Output

---

## 🚨 Important Note
This project is for educational purposes only.
Scraping certain websites might violate their terms of service — use responsibly!

---

## 💬 Contributing
Feel free to contribute by submitting a pull request or reporting any issues!

---

## 🌟 Contact
If you have any questions or feedback, reach out to me at olisaurabh00@gmail.com.

---

## ⭐ If you find this project useful, don't forget to give it a star! 🌟
