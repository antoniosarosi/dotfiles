set fish_greeting ""

# Aliases

alias grep "grep --color=auto"
alias cat "ccat -G Plaintext="blink" -G Keyword="purple" -G String="darkgreen" -G Punctuation="brown" -G Comment="faint""
alias ls "exa --group-directories-first"
alias tree "exa -T"

# Agnoster

set -g theme_display_user yes
set -g theme_hide_hostname no
set -g color_user_bg magenta
set -g color_user_str black

# Spacefish

set SPACEFISH_PROMPT_ADD_NEWLINE false
set SPACEFISH_PROMPT_PREFIXES_SHOW false
set SPACEFISH_PROMPT_DEFAULT_PREFIX " "
set SPACEFISH_PROMPT_DEFAULT_SUFFIX " "
set SPACEFISH_USER_SHOW always
set SPACEFISH_USER_COLOR green
set SPACEFISH_HOST_SHOW always
set SPACEFISH_PROMPT_ORDER time user host dir git package node ruby golang php rust haskell julia elixir docker aws venv conda pyenv dotnet kubecontext exec_time line_sep battery vi_mode jobs exit_code char  
