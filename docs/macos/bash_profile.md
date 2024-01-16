```
alias ll='ls -alF'
alias e='exit'
alias c='clear'
alias dockerps='docker ps --format "{{.ID}}\t{{.Names}}"'


# Git branch in prompt.
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\033[34m\]\t\[\033[00m\] \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "


[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"
source ~/.git-completion.bash

source /Users/lian/python3.11-venv/bin/activate

# Added by Toolbox App
export PATH="$PATH:/usr/local/bin"


eval "$(/usr/local/bin/brew shellenv)"
# Set PATH, MANPATH, etc., for Homebrew.
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"


# export http_proxy="socks5://127.0.0.1:1080"
# export https_proxy="socks5://127.0.0.1:1080"
```
