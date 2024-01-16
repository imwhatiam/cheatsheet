vi ~/.vimrc

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

Plugin 'ycm-core/YouCompleteMe'

Plugin 'yegappan/mru'
nnoremap <silent> <F7> :MRU<CR>


Plugin 'ntpeters/vim-better-whitespace'
nnoremap <silent> <F8> :StripWhitespace<CR>


Plugin 'Exafunction/codeium.vim'
imap <script><silent><nowait><expr> <C-h> codeium#Accept()


Plugin 'yegappan/grep'
nnoremap <silent> <F12> :Rgrep<CR>
let Grep_Default_Filelist = '*.py *.html *.js'


Plugin 'vim-syntastic/syntastic'
" pip3 install flake8
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['flake8']
let g:syntastic_python_flake8_args="--max-line-length=120"


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" To ignore plugin indent changes, instead use:
" filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line



map <F5> :call PRUN()<CR>
func! PRUN()
    exec "w"
    if &filetype == 'python'
        exec "!python %"
    endif
endfunc


" Syntax highlighting
syntax on

set number
set textwidth=79

" highlight
:set listchars=tab:>-,trail:-

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

set statusline+=%F
```
