# 🔥 AI Resume Roaster

An AI-powered Streamlit application that provides brutally honest, witty resume feedback in Hinglish (Hindi + English). Get your resume roasted by AI and receive constructive suggestions to land your dream job!

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red?style=flat-square&logo=streamlit)
![Azure AI](https://img.shields.io/badge/Azure%20AI-GPT--4-green?style=flat-square&logo=microsoft)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 🌟 Features

- **AI-Powered Analysis**: Uses GitHub's GPT-4o model for intelligent resume evaluation
- **Hinglish Feedback**: Get feedback in a fun mix of Hindi and English
- **PDF & Text Support**: Upload resumes in PDF or TXT format
- **Role-Specific Analysis**: Tailored feedback based on your target job role
- **Modern UI**: Clean, dark-themed interface with smooth animations
- **Instant Results**: Fast processing with real-time feedback

## 🎯 What Does It Do?

1. **Upload Your Resume** - PDF or TXT format supported
2. **Specify Target Role** - Enter the job you're applying for
3. **Get Roasted** - Receive brutally honest but constructive feedback
4. **Improve & Repeat** - Use suggestions to enhance your resume

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS
- **AI Model**: OpenAI GPT-4o via GitHub AI Inference
- **PDF Processing**: PyPDF2
- **Package Management**: UV (ultra-fast Python package installer)
- **Environment Management**: python-dotenv

## 🚀 Quick Start with UV

### Prerequisites

- Python 3.13+
- UV package manager
- GitHub Personal Access Token
- Internet connection

### Step 1: Install UV

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Step 2: Clone & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/ai-resume-roaster.git
cd ai-resume-roaster

# Install dependencies using UV
uv sync

# Create virtual environment (if not automatically created)
uv venv
```

### Step 3: Environment Configuration

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` with your actual API keys:
```env
GITHUB_TOKEN=your_github_personal_access_token_here
GEMINI_API_KEY=your_google_ai_studio_api_key_here
```

### Step 4: Run the Application

```bash
# Start the Streamlit app
uv run streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## 🔑 API Keys Setup

### GitHub Personal Access Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes: `read:user`, `user:email`
4. Copy the generated token
5. Add to `.env` file

### Google Gemini API (Optional Backup)

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create new API key
3. Copy the key
4. Add to `.env` file

## 📁 Project Structure

```
ai-resume-roaster/
├── main.py                 # Main Streamlit application
├── ai_client.py            # AI model interaction
├── file_processor.py       # PDF/TXT file handling
├── config.py              # Configuration constants
├── style_loader.py        # CSS loading utilities
├── styles.css             # Custom styling
├── pyproject.toml         # UV project configuration
├── .env                   # Environment variables (not in repo)
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── README.md              # This file
└── __pycache__/           # Python cache (auto-generated)
```

## 🎨 Customization

### Modify AI Behavior

Edit `ai_client.py` to change:
- Response tone and style
- Word limits
- Evaluation criteria
- Language preferences

### UI Customization

Edit `styles.css` to customize:
- Color schemes
- Fonts and typography
- Layout and spacing
- Animations and effects

### Configuration

Edit `config.py` to modify:
- App title and description
- File upload limits
- AI model parameters

## 🐛 Troubleshooting

### Common Issues

**"API token not found"**
- Check your `.env` file exists
- Verify API keys are correctly formatted
- Ensure no extra spaces in the keys

**"Failed to get AI response"**
- Verify internet connection
- Check GitHub token permissions
- Try regenerating your GitHub token

**"File does not have any content"**
- Ensure PDF is not image-based
- Try converting PDF to text first
- Check file encoding for TXT files

**UV sync fails**
- Update UV: `uv self update`
- Clear cache: `uv cache clean`
- Try: `uv sync --no-install-project`

### Performance Tips

- Use smaller PDF files (< 5MB)
- Ensure stable internet connection
- Close unnecessary browser tabs

## 🚀 Deployment

### Local Development
```bash
uv run streamlit run main.py --server.port 8501
```

### Production Deployment
See the deployment section below for Streamlit Cloud hosting.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Pushkar Shukla**
- GitHub: [@pushkarshukla](https://github.com/pushkarshukla)
- Email: pushkar@example.com

## 🙏 Acknowledgments

- OpenAI for GPT-4 model
- GitHub for AI inference platform
- Streamlit for the amazing web framework
- UV for lightning-fast package management

## 📊 Usage Stats

- Supported file formats: PDF, TXT
- Average processing time: 3-5 seconds
- Maximum file size: 10MB
- Response length: 300-500 words

---

**Made with ❤️ and a lot of ☕ by Pushkar Shukla**

*Get ready to have your resume roasted! 🔥*