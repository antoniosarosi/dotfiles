-- Line numbers
vim.opt.nu = true
vim.opt.relativenumber = true

-- Tabs
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true

-- Indentation
vim.opt.smartindent = true

-- Don't wrap text
vim.opt.wrap = false

-- Searching
vim.opt.hlsearch = false
vim.opt.incsearch = true

-- Colors
vim.opt.termguicolors = true

-- Vertical markers
vim.opt.signcolumn = "yes"
vim.opt.colorcolumn = "80"

-- Don't load netrw because we use nvim-tree
vim.g.load_netrw = 1
vim.g.load_netrwPlugin = 1
