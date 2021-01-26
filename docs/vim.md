# vim 命令

## 光标移动

| 操作  | 说明                                  | 备注                                  |
| ---   | -------------------                   | --------------------------            |
| `+`   | 光标移动到下一行非空格处              |                                       |
| `-`   | 光标移动到上一行非空格处              |                                       |
| `0`   | 光标移动到这一行的最前面字符处        | 或功能键 **Home**                         |
| `$`   | 光标移动到这一行的最后面字符处        | 或功能键 **End**，`$`在正则里面表示是结尾 |
| `H`   | 光标移动到屏幕最上方一行的第一个字符  | `H`是 _header_的缩写                    |
| `M`   | 光标移动到屏幕中夬那一行的第一个字符  | `M`是 _middle_的缩写                    |
| `L`   | 光标移动到屏幕最下方一行的第一个字符  | `L`是 _last_的缩写                      |
| `*`   | 光标移动到下一个, 光标当前所在的单词  | `#`是移动到下一个                     |    

```
Vim光标以单词为单位移动

w 或 W：光标移动至下一个单词的单词首
b 或 B：光标移动至上一个单词的单词首
e 或 E：光标移动至下一个单词的单词尾
nw 或 nW：n 为数字，表示光标向右移动 n 个单词
nb 或 nB：n 为数字，表示光标向左移动 n 个单词

Vim光标移动至行首或行尾

0 或 ^：光标移动至当前行的行首
$：光标移动至当前行的行尾
n$：光标移动至当前行只有 n 行的行尾，n为数字

Vim光标移动至指定字符

fx：光标移动至当前行中下一个 x 字符处
Fx：光标移动至当前行中下一个 x 字符处

Vim光标移动到指定行

gg：光标移动到文件开头
G：光标移动至文件末尾
nG：光标移动到第 n 行，n 为数字
:n：编辑模式下使用的快捷键，可以将光标快速定义到指定行的行首
```

## 查找和替换

```
:%s/^\s*[0-9]*\s*//gc
```
将每行以0或多个空格开始、中间包含0或多个数字、并以0或多个空格结束的字符串替换为空。

> `%`代表针对被编辑文件的每一行进行后续操作；`^` 表示行首（`$` 表示行尾），`\s` 表示空格，`[0-9]` 表示0~9的数字，`*` 表示0或多个

* 查找 `aa` 或 `bb`：`/aa\|bb`

* 替换前显示提示字符给用户确认 (confirm) 是否需要替换：`:%s/string1/string2/gc`

* 删除空行：`%s/^\n//gc`

* 删除行尾的空格：`:%s/ *$//gc` or `:%s/\s\+$//gc`

* 删除行首的空格：` :%s/^ *//gc`

* 行首添加字符串 `string`：`%s/^/string/gc`

* 行尾添加字符串 `string`：`%s/$/string/gc`

* 在2-7行之间，将ddd替换成fff：`:2,7s/ddd/fff/g`

* 在6~10行的行首加一个 `#` 号：`:6,10s/^/#/gc`

```
\        取消后面所跟字符的特殊含义。比如 \[vim\] 匹配字符串“[vim]”

[]       匹配其中之一。比如 [vim] 匹配字母“v”、“i”或者“m”，[a-zA-Z] 匹配任意字母

[^]      匹配非其中之一。比如 [^vim] 匹配除字母“v”、“i”和“m”之外的所有字符

.        匹配任意字符

*        匹配前一字符大于等于零遍。比如 vi*m 匹配“vm”、“vim”、“viim”……

\+       匹配前一字符大于等于一遍。比如 vi\+m 匹配“vim”、“viim”、“viiim”……

\?       匹配前一字符零遍或者一遍。比如 vi\?m 匹配“vm”或者“vim”

^        匹配行首。例如 /^hello 查找出现在行首的单词 hello

$        匹配行末。例如 /hello$ 查找出现在行末的单词 hello

\(\)     括住某段正规表达式

\数字    重复匹配前面某段括住的表达式。例如 \(hello\).*\1 匹配一个开始和末尾都是“hello”，中间是任意字符串的字符串
```

## vim 配置

### 配置 Markdown 文件预览

```
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
sudo npm -g install instant-markdown-d
```

add the following lines to _.vimrc_

```
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'suan/vim-instant-markdown'
```

then

```
:PluginInstall
```

### .vimrc

```
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'


Plugin 'Yggdroot/indentLine'


Plugin 'kien/ctrlp.vim'

" *********************************************
" ctrlp
" *********************************************
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
" 设置过滤不进行查找的后缀名
let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn|pyc|html|js)$'


Plugin 'majutsushi/tagbar'
" 启动时自动focus
 map <F4> :TagbarToggle<CR>
let g:tagbar_auto_faocus =1
" 启动指定文件时自动开启tagbar
autocmd BufReadPost *.cpp,*.c,*.h,*.hpp,*.cc,*.cxx call tagbar#autoopen()


Plugin 'ycm-core/YouCompleteMe'
" *********************************************
" YCM插件相关
" *********************************************
let g:ycm_autoclose_preview_window_after_completion=1
" 跳转到定义处
map <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>
" 默认tab、s-tab和自动补全冲突
let g:ycm_key_list_select_completion = ['<TAB>', '<c-n>', '<Down>']
let g:ycm_key_list_previous_completion = ['<S-TAB>', '<c-p>', '<Up>']
let g:ycm_auto_trigger = 1


Plugin 'scrooloose/nerdtree'
map <F2> :NERDTreeToggle<CR>
let NERDTreeIgnore = [".*\.pyc",".*\.swp",".*\.png",".*\.gif",".*\.jpg",".*\.ico","tags",".*\.tar.gz"]
let NERDTreeIgnore=['\.pyc', '\~$', '\.swo$', '\.swp$', '\.git', '\.hg', '\.svn', '\.bzr', '\.DS_Store', '\.db']
let NERDTreeWinSize=20
" How can I close vim if the only window left open is a NERDTree?
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif


Plugin 'yegappan/grep'
nnoremap <silent> <F12> :Rgrep<CR>
let Grep_Default_Filelist = '*.py *.html *.js'


Plugin 'yegappan/mru'
nnoremap <silent> <F7> :MRU<CR>


Plugin 'ntpeters/vim-better-whitespace'
nnoremap <silent> <F8> :StripWhitespace<CR>


" python -m pip install flake8
"
" cat ~/.config/flake8
" [flake8]
" max-line-length = 120
Plugin 'vim-syntastic/syntastic'
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['flake8']


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"

map <F5> :call PRUN()<CR>
func! PRUN()
    exec "w"
    if &filetype == 'python'
        exec "!python %"
    endif
endfunc

syntax on " Syntax highlighting

set number
set textwidth=79

" Auto indent
set autoindent

" Smart indent
set smartindent

" Ignore case when searching
set ignorecase

" Remember info about open buffers on close
set viminfo^=%

" Set 7 lines to the cursor - when moving vertically using j/k
set scrolloff=7

" Always show current position
set ruler

" When searching try to be smart about cases
set smartcase

" Highlight search results
set hlsearch
:nnoremap <silent> <Space> :nohlsearch<Bar>:echo<CR>

" Return to last edit position when opening files (You want this!)
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif
" Remember info about open buffers on close
set viminfo^=%

set backspace=2

set encoding=utf-8

set clipboard=unnamed

" *********************************************
" 分割布局相关
" *********************************************
set splitbelow
set splitright
"快捷键，ctrl+l切换到左边布局，ctrl+h切换到右边布局
"ctrl+k切换到上面布局，ctrl+j切换到下面布局
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
```
