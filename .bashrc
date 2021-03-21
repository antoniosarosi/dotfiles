#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
# alias cat='ccat -G Plaintext="blink" -G Keyword="purple" -G String="darkgreen" -G Punctuation="brown" -G Comment="faint"'
# alias ls='exa --group-directories-first'
alias ls='ls --color=auto'
# alias tree='exa -T'

# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\] '

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# __conda_setup="$('/home/antonio/miniconda2/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
# if [ $? -eq 0 ]; then
#     eval "$__conda_setup"
# else
#     if [ -f "/home/antonio/miniconda2/etc/profile.d/conda.sh" ]; then
#         . "/home/antonio/miniconda2/etc/profile.d/conda.sh"
#     else
#         export PATH="/home/antonio/miniconda2/bin:$PATH"
#     fi
# fi
# unset __conda_setup
# <<< conda initialize <<<

