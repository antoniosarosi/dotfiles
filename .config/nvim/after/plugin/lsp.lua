local lsp = require('lsp-zero').preset({})
local lspconfig = require('lspconfig')
local cmp = require("cmp")

lsp.ensure_installed({
    "rust_analyzer",
    "zls",
    "clangd",
    "gopls",
    "tsserver",
    "pyright",
    "hls",
    "lua_ls",
})

lsp.on_attach(function(client, bufnr)
  lsp.default_keymaps({buffer = bufnr})

  vim.keymap.set("n", "<leader>lr", vim.lsp.buf.rename)
  vim.keymap.set("n", "<leader>lf", vim.lsp.buf.format)
end)

lspconfig.lua_ls.setup(lsp.nvim_lua_ls())

lspconfig.gopls.setup {
    settings = {
        gopls = {
            semanticTokens = true,
        }
    },
}

lsp.setup()

local select_behavior = {behavior = cmp.SelectBehavior.Select}
cmp.setup({
    mapping = {
        ["<CR>"] = cmp.mapping.confirm({select = false}),
        ["<TAB>"] = cmp.mapping.select_next_item(select_behavior),
        ["<S-TAB>"] = cmp.mapping.select_prev_item(select_behavior),
    }
})
