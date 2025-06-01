# 🔥 AI Resume Roaster

> Get your resume roasted by AI and make it job-ready! 🚀

A fun and educational Streamlit web application that uses Artificial Intelligence to give you brutally honest (but helpful!) feedback on your resume. Perfect for learning about AI, improving your resume, and having a good laugh!

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red?style=flat-square&logo=streamlit)
![AI](https://img.shields.io/badge/AI-GPT--4-green?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🎯 What Does This App Do?

Think of this as your **friendly (but slightly mean) robot friend** who helps you improve your resume:

1. **📄 Upload Your Resume** - Drop in your PDF or text file
2. **🎯 Tell It Your Dream Job** - What position are you targeting?
3. **🤖 Let AI Work Its Magic** - The AI reads and analyzes your resume
4. **🔥 Get Roasted (Nicely!)** - Receive funny but helpful feedback in Hinglish
5. **💪 Make It Better** - Use the suggestions to improve your resume

**Important:** This is a **learning project** - the AI is trying to be funny and educational, so don't take the "roasts" too seriously! Focus on the helpful tips.

---

## ✨ Cool Features

- **🧠 Smart AI Analysis** - Uses advanced AI to understand your resume
- **😄 Hinglish Feedback** - Get feedback in a fun mix of Hindi and English
- **📱 Easy Upload** - Just drag and drop your PDF or text file
- **🎨 Beautiful Interface** - Modern, dark-themed design that's easy on the eyes
- **⚡ Super Fast** - Get results in seconds
- **🆓 Completely Free** - No hidden costs or subscriptions

---

## 🚀 How to Get Started (Step-by-Step for Beginners)

Don't worry if you're new to coding! We'll walk you through everything step by step.

### 🔧 What You'll Need

- A computer (Windows, Mac, or Linux)
- Internet connection
- About 10-15 minutes of your time
- Your resume file (PDF or text)

### Step 1: Install UV (The Magic Helper Tool)

UV is a super-fast tool that helps us install everything we need. Think of it as your coding assistant!

**For Windows Users:**
1. Press `Windows Key + R`
2. Type `powershell` and press Enter
3. Copy and paste this command, then press Enter:
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**For Mac Users:**
1. Press `Cmd + Space`, type `terminal`, and press Enter
2. Copy and paste this command, then press Enter:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**For Linux Users:**
1. Open your terminal
2. Copy and paste this command, then press Enter:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*You only need to do this once!*

### Step 2: Download the Project

**Option A: Download as ZIP (Easiest)**
1. Click the green "Code" button on this GitHub page
2. Select "Download ZIP"
3. Extract the ZIP file to a folder like `Desktop` or `Documents`

**Option B: Using Git (If you know Git)**
```bash
git clone https://github.com/your-username/ai-resume-roaster.git
cd ai-resume-roaster
```

### Step 3: Open Terminal/Command Prompt in Project Folder

**Windows:**
1. Open the project folder
2. Hold `Shift` and right-click in an empty area
3. Select "Open PowerShell window here"

**Mac:**
1. Open Finder and navigate to the project folder
2. Right-click the folder and select "New Terminal at Folder"

**Linux:**
1. Navigate to the project folder
2. Right-click and select "Open in Terminal"

### Step 4: Install Everything Automatically

In your terminal/command prompt, type this command:
```bash
uv sync
```

This magical command will:
- ✅ Download all the tools our app needs
- ✅ Set up everything automatically
- ✅ Make sure everything works together

*This might take a minute or two. Perfect time for a coffee break! ☕*

### Step 5: Get Your Secret Keys (Important!)

Our app needs special "keys" to talk to the AI services. Think of them as passwords for AI.

#### 5.1: Create Your Environment File

1. In the project folder, create a new file called `.env` (yes, with a dot at the beginning)
2. Open it with any text editor (Notepad, TextEdit, etc.)
3. Copy and paste these lines:

```env
GITHUB_TOKEN=your_github_token_will_go_here
GEMINI_API_KEY=your_gemini_key_will_go_here
```

#### 5.2: Get Your GitHub Token

1. Go to [GitHub.com](https://github.com) and log in (create account if needed)
2. Click your profile picture → Settings
3. Scroll down and click "Developer settings"
4. Click "Personal access tokens" → "Tokens (classic)"
5. Click "Generate new token (classic)"
6. Give it a name like "AI Resume Roaster"
7. Select expiration (30 days is fine for testing)
8. Check the box for "read:user"
9. Click "Generate token"
10. **IMPORTANT:** Copy the token immediately and replace `your_github_token_will_go_here` in your `.env` file

#### 5.3: Get Your Gemini API Key (Optional but Recommended)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and replace `your_gemini_key_will_go_here` in your `.env` file

**Your `.env` file should now look like this:**
```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GEMINI_API_KEY=AIxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 6: Launch Your App! 🚀

In your terminal/command prompt, type:
```bash
uv run streamlit run main.py
```

**🎉 Congratulations!** Your browser should automatically open and show your AI Resume Roaster app at `http://localhost:8501`

If the browser doesn't open automatically, just copy that link and paste it into your browser.

---

## 📖 How to Use the App

Using the app is super simple:

### 1. Upload Your Resume 📄
- Click the "Choose your resume file" button
- Select your resume (PDF or TXT format)
- Wait for the green success message

### 2. Enter Your Target Job 🎯
- In the "Target Role" box, type the job you want
- Examples: "Software Developer", "Marketing Manager", "Data Scientist"

### 3. Get Your Roast! 🔥
- Click the big "🔥 Roast My Resume!" button
- Wait a few seconds for the AI to work its magic
- Read your personalized feedback

### 4. Improve and Try Again 💪
- Use the suggestions to improve your resume
- Upload the improved version and see how you did!

---

## 🎨 What's Inside the Project? (For Curious Minds)

```
ai-resume-roaster/
├── main.py                 # 🧠 The brain of the app
├── ai_client.py            # 🤖 Talks to the AI
├── file_processor.py       # 📄 Reads your resume files
├── config.py              # ⚙️ App settings
├── style_loader.py        # 🎨 Makes the app look pretty
├── styles.css             # 💄 All the beautiful colors and fonts
├── requirements.txt       # 📋 List of tools we need
├── .env                   # 🔐 Your secret keys (keep this private!)
├── README.md              # 📖 This helpful guide
└── pyproject.toml         # 📦 Project configuration
```

---

## 🛠️ Troubleshooting (When Things Go Wrong)

### "Command not found: uv"
**Problem:** UV isn't installed correctly.
**Solution:** Go back to Step 1 and reinstall UV.

### "API token not found"
**Problem:** Your `.env` file isn't set up correctly.
**Solutions:**
- ✅ Make sure the file is named exactly `.env` (with the dot)
- ✅ Check that your GitHub token is correct
- ✅ Make sure there are no extra spaces around the token
- ✅ Try regenerating your GitHub token

### "Error reading file"
**Problem:** Your resume file might be corrupted or in the wrong format.
**Solutions:**
- ✅ Try saving your resume as a different PDF
- ✅ Make sure the file isn't password-protected
- ✅ Try converting it to a text file (.txt)

### "Failed to get AI response"
**Problem:** Network or API issues.
**Solutions:**
- ✅ Check your internet connection
- ✅ Make sure your API keys are valid
- ✅ Try again in a few minutes

### App Won't Start
**Problem:** Something went wrong with installation.
**Solutions:**
```bash
# Try these commands one by one:
uv cache clean
uv sync --no-install-project
uv run streamlit run main.py
```

### Still Having Problems?
- 📧 Create an issue on this GitHub repository
- 🔍 Google the error message
- 💬 Ask a friend who knows coding!

---

## 🌟 Making It Your Own

Want to customize the app? Here are some fun ideas:

### Change the Roasting Style
Edit `ai_client.py` to make the AI:
- More encouraging and less sarcastic
- Focus on specific industries
- Use different languages
- Give longer or shorter feedback

### Customize the Look
Edit `styles.css` to:
- Change colors and themes
- Modify fonts and sizes
- Add animations
- Create your own design

### Add New Features
Some ideas for advanced users:
- Support for more file types (Word docs, etc.)
- Resume scoring system
- Comparison with job descriptions
- Export feedback as PDF

---

## 🚀 Want to Share Your App Online?

Once you're happy with your app, you can share it with the world for free!

### Deploy to Streamlit Cloud (Free!)

1. **Push your code to GitHub**
```bash
git add .
git commit -m "My awesome resume roaster app!"
git push origin main
```

2. **Deploy on Streamlit Cloud**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"
- Select your repository
- Add your API keys in the "Secrets" section
- Click "Deploy!"

3. **Share your app**
- Get a public URL like `https://your-username-ai-resume-roaster.streamlit.app`
- Share with friends, family, and potential employers!

---

## 📚 Learn More

Want to dive deeper? Check out these resources:

### For Beginners
- [Python Basics](https://www.python.org/about/gettingstarted/)
- [Streamlit Tutorial](https://docs.streamlit.io/get-started)
- [What is AI?](https://www.ibm.com/topics/artificial-intelligence)

### For Advanced Users
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Azure AI Services](https://docs.microsoft.com/en-us/azure/cognitive-services/)
- [Streamlit Components](https://docs.streamlit.io/develop/concepts/architecture/components)

---

## 🤝 Contributing to the Project

Found a bug? Have a cool idea? Want to help make this project better?

1. **Report Issues:** Create an issue on GitHub
2. **Suggest Features:** Tell us what you'd like to see
3. **Submit Code:** Fork the repo and create a pull request
4. **Share:** Tell others about this project!

All skill levels welcome - from beginners to experts! 🌟

---

## 📜 License & Legal Stuff

This project is open source and free to use under the MIT License. This means you can:
- ✅ Use it for personal projects
- ✅ Modify it however you want
- ✅ Share it with others
- ✅ Use it to learn and teach

**Just remember:** This is an educational project. The AI feedback is meant to be fun and helpful, but always use your own judgment when making resume decisions!

---

## 👨‍💻 About the Creator

**Pushkar Shukla** - A passionate developer who loves creating educational tools and making technology accessible to everyone.

- 🐙 **GitHub:** [@pushkarshukla](https://github.com/pushkarshukla)
- 📧 **Email:** pushkar@example.com
- 💼 **LinkedIn:** Connect for more awesome projects!

---

## 🙏 Special Thanks

This project wouldn't be possible without these amazing tools and services:

- **🤖 OpenAI & GitHub** - For providing the AI models
- **🚀 Streamlit** - For making web apps so easy to build
- **⚡ UV** - For lightning-fast Python package management
- **🎨 Google Fonts** - For beautiful typography
- **🌟 The Open Source Community** - For all the awesome libraries

---

## 📊 Project Stats

- 📁 **File Formats Supported:** PDF, TXT
- ⚡ **Average Processing Time:** 3-5 seconds
- 📏 **Feedback Length:** 300-500 words
- 🌍 **Languages:** Hinglish (Hindi + English)
- 💾 **Max File Size:** 10MB
- 🆓 **Cost:** Completely free!

---

## 🎉 Ready to Get Started?

Scroll back up to [Step 1](#step-1-install-uv-the-magic-helper-tool) and let's build something awesome together!

**Remember:** The goal is to learn, have fun, and improve your resume. Don't stress if something doesn't work perfectly the first time - that's all part of the learning process! 💪

---

*Made with ❤️, lots of ☕, and a dash of AI magic by Pushkar Shukla*

**Happy Resume Roasting! 🔥**