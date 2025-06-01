"""Configuration constants for the Resume Roaster application."""

# ============================================================================
# APPLICATION METADATA
# ============================================================================

APP_TITLE = "AI Resume Roaster"                    # Main app title
APP_CREATOR = "Pushkar Shukla"                     # Creator name for badge
APP_DESCRIPTION = "Upload your resume and get AI powered roasting!"  # App description

# ============================================================================
# FILE UPLOAD SETTINGS
# ============================================================================

ALLOWED_FILE_TYPES = ["pdf", "txt"]                # Supported file formats
MAX_FILE_SIZE = 10                                  # Maximum file size in MB

# ============================================================================
# AI MODEL CONFIGURATION
# ============================================================================

AI_TEMPERATURE = 1.0                               # Creativity level (0.0-2.0)
AI_TOP_P = 1.0                                     # Token diversity (0.0-1.0)
MAX_RESPONSE_WORDS = 500                           # Response length limit