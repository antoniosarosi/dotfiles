call plug#begin('~/.config/nvim/plugged')
    " Syntax support
    Plug 'sheerun/vim-polyglot'
    " Autopairs
    Plug 'jiangmiao/auto-pairs'
    " File explorer
    Plug 'scrooloose/NERDTree'    
    " Icons
    Plug 'ryanoasis/vim-devicons'
    " Intellisense
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Airline
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    " Indent guides
    Plug 'Yggdroot/indentLine' 
    " Git integration
    Plug 'mhinz/vim-signify'
    " Autoclose tags
    Plug 'alvan/vim-closetag'
    " Comment code
    Plug 'tpope/vim-commentary'

    " Themes
    Plug 'joshdick/onedark.vim'
    Plug 'kaicataldo/material.vim'
call plug#end()
