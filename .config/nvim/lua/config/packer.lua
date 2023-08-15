-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  -- Packer
  use 'wbthomason/packer.nvim'

  -- Themes
  use 'navarasu/onedark.nvim'
  use 'Mofiqul/dracula.nvim'

  -- Fonts
  use 'nvim-tree/nvim-web-devicons'

  -- Indent guides
  use "lukas-reineke/indent-blankline.nvim"
  -- Auto-close parenthesis and brackets
  use "windwp/nvim-autopairs"
  -- Comment lines
  use "tpope/vim-commentary"

  -- Status bar
  use 'nvim-lualine/lualine.nvim'
  -- "Tabs support" (move between buffers)
  use 'romgrk/barbar.nvim'

  -- File tree
  use 'nvim-tree/nvim-tree.lua'
  -- Fuzzy finder
  use {
    'nvim-telescope/telescope.nvim',
    tag = '0.1.2',
    requires = {'nvim-lua/plenary.nvim'},
  }
  -- Git support
  use 'lewis6991/gitsigns.nvim'

  -- Syntax highlight
  use {'nvim-treesitter/nvim-treesitter', run = ':TSUpdate'}
  use 'nvim-treesitter/playground'

  -- LSP
  use {
    'VonHeikemen/lsp-zero.nvim',
    branch = 'v2.x',
    requires = {
      -- LSP Support
      {'neovim/nvim-lspconfig'},             -- Required
      {'williamboman/mason.nvim'},           -- Optional
      {'williamboman/mason-lspconfig.nvim'}, -- Optional

      -- Autocompletion
      {'hrsh7th/nvim-cmp'},     -- Required
      {'hrsh7th/cmp-nvim-lsp'}, -- Required
      {'L3MON4D3/LuaSnip'},     -- Required
    }
  }
end)
