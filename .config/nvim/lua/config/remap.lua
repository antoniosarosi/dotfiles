vim.g.mapleader = " "

-- Open netrw
-- vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

-- Toggle Nvim Tree
vim.keymap.set("n", "<leader>e", vim.cmd.NvimTreeToggle)

-- Save with CTRL S
vim.keymap.set("n", "<C-s>", ":w<CR>")
vim.keymap.set("i", "<C-s>", "<Esc>:w<CR>")

-- Esc with JK
vim.keymap.set("i", "jk", "<Esc>")
vim.keymap.set("i", "kj", "<Esc>")

-- Indent with tab
vim.keymap.set("v", "<TAB>", ">gv")
vim.keymap.set("v", "<S-TAB>", "<gv")
vim.keymap.set("v", ">", ">gv")
vim.keymap.set("v", "<", "<gv")

-- Move selected lines up and down
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")

-- Move between windows
vim.keymap.set("n", "<C-l>", "<C-w>l")
vim.keymap.set("n", "<C-h>", "<C-w>h")
vim.keymap.set("n", "<C-j>", "<C-w>j")
vim.keymap.set("n", "<C-k>", "<C-w>k")

-- Resize windows
vim.keymap.set("n", "<M-h>", ":vertical resize +5<CR>")
vim.keymap.set("n", "<M-l>", ":vertical resize -5<CR>")
vim.keymap.set("n", "<M-j>", ":horizontal resize +5<CR>")
vim.keymap.set("n", "<M-k>", ":horizontal resize -5<CR>")

-- Close buffer
-- vim.keymap.set("n", "<C-b>", ":bd<CR>")

-- Move between buffers
-- vim.keymap.set("n", "<TAB>", ":bnext<CR>")
-- vim.keymap.set("n", "<S-TAB>", ":bprevious<CR>")

-- Stay in the middle while half page scrolling
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

-- Keep the cursor in the middle while searching
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Paste buffer over selection without loosing buffer
vim.keymap.set("x", "<leader>p", "\"_dP")

-- Copy yanks to clipboard
vim.keymap.set("n", "<leader>y", "\"+y")
vim.keymap.set("v", "<leader>y", "\"+y")
vim.keymap.set("n", "<leader>Y", "\"+Y")

-- Replace word or text
vim.keymap.set("n", "<leader>r", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
vim.keymap.set("v", "<leader>r", "\"hy:%s/<C-r>h/<C-r>h/g<left><left>")

-- Highlight search
vim.keymap.set("n", "<leader>s", ":set hlsearch<CR>ma/<C-r><C-w><Esc>`a:set nohlsearch")
vim.keymap.set("v", "<leader>s", "\"hy:set hlsearch<CR>ma/<C-r>h<Esc>`a:set nohlsearch")

-- Terminal
vim.keymap.set("n", "<leader>t", ":belowright split +resize-20 | terminal<CR>")
vim.keymap.set("t", "<C-n>", "<C-\\><C-n>")
vim.keymap.set("t", "<C-k>", "<C-\\><C-n><C-w>k")
