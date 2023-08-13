require'barbar'.setup {
    sidebar_filetypes = {
        NvimTree = true,
    }
}

vim.keymap.set("n", "<TAB>", ":BufferNext<CR>")
vim.keymap.set("n", "<S-TAB>", ":BufferPrevious<CR>")
vim.keymap.set("n", "<C-b>", ":BufferClose<CR>")
vim.keymap.set("n", "<A-,>", ":BufferMovePrevious<CR>")
vim.keymap.set("n", "<A-.>", ":BufferMoveNext<CR>")
vim.keymap.set("n", "<A-p>", ":BufferPin<CR>")
vim.keymap.set("n", "<leader>b", ":BufferCloseAllButCurrent<CR>")
