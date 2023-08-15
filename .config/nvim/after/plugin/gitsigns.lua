require('gitsigns').setup()

vim.keymap.set("n", "<leader>gp", ":Gitsigns prev_hunk<CR>")
vim.keymap.set("n", "<leader>gn", ":Gitsigns next_hunk<CR>")
vim.keymap.set("n", "<leader>gh", ":Gitsigns preview_hunk<CR>")
vim.keymap.set("n", "<leader>gd", ":Gitsigns diffthis<CR>")
vim.keymap.set("n", "<leader>gr", ":Gitsigns reset_hunk<CR>")
vim.keymap.set("n", "<leader>gb", ":Gitsigns blame_line<CR>")
