# GovAssist AI ✨

![GovAssist AI Banner](banner.png)

> AI-powered Flask portal recommending Indian government schemes based on user attributes like age, income, gender, occupation, and region.

---

## 🚀 Live Demo

**→** *Coming soon with deployment guide*

---

## 🔍 Project Features

* 💼 Scheme recommendations tailored for citizens based on eligibility
* ⚖️ Filters: Age, Income, Gender, Occupation, Region
* 📝 Form-based data input (HTML + Flask)
* 📅 Clean CSV-based backend (easily extendable)


---

## ⚙️ Technologies Used

* Python 3.10+
* Flask
* Pandas
* HTML5 + CSS3

---

## 🎓 Use Case

> This project aims to bridge the awareness gap about beneficial schemes available for Indian citizens, helping students, farmers, women, unemployed youth, and more.

---

## 📂 Folder Structure

```
GovAssistAI/
|├── app.py
|├── scheme_data.csv
|├── templates/
|   |├── index.html
|   └── result.html
|└── static/ (optional)
```

---

## 📊 Dataset

* **Source**: Manually curated from government portals like [India.gov.in](https://www.india.gov.in), [pmindia.gov.in](https://www.pmindia.gov.in), and scheme-specific portals
* **Format**: CSV with columns like `Name`, `Min_Age`, `Max_Age`, `Gender`, `Income_Range`, `Occupation`, etc.

> ℹ️ All scheme information is for demonstration purposes only and may not reflect real-time official details.

---

## 📚 How to Run Locally

1. **Clone Repo**:

   ```bash
   git clone https://github.com/MayuriM26/GovAssitAI.git
   cd GovAssitAI
   ```
2. **Setup Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install Requirements**:

   ```bash
   pip install flask pandas
   ```
4. **Run App**:

   ```bash
   python app.py
   ```
5. **Visit in Browser**:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📷 Screenshots

![Form Page](screenshots/form.png)
![Scheme Result](screenshots/results.png)

---

## 🌟 Credits

Created with ❤️ by [Mayuri Mohite](https://github.com/MayuriM26)

---

## 🚫 Disclaimer

This app is for **educational/demo purposes only** and does not officially connect to any government database.

---

## 📊 GitHub Tags

`#flask` `#python` `#recommendation-system` `#government-schemes` `#ai` `#btech-project` `#citizen-portal`
