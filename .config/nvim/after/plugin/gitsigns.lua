require('gitsigns').setup()

vim.keymap.set("n", "<leader>hp", ":Gitsigns prev_hunk<CR>")
vim.keymap.set("n", "<leader>hn", ":Gitsigns next_hunk<CR>")
vim.keymap.set("n", "<leader>hh", ":Gitsigns preview_hunk<CR>")
vim.keymap.set("n", "<leader>hd", ":Gitsigns diffthis<CR>")
