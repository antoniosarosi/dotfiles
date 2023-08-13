require("onedark").setup {
    style = "darker",
    -- transparent = "true",
}

local color = "onedark"
vim.cmd.colorscheme(color)

local function set_color(group, options)
    vim.api.nvim_set_hl(0, group, options)
end

if color == "onedark" then
    set_color("@operator", { fg = '#56B6C2' })
    set_color("@field", { fg = '#E06C75' })
    set_color("@string.escape", { fg = '#56B6C2' })
    set_color("@punctuation.delimiter", { fg = '#56B6C2' })
    set_color("@constructor", { link = "@type" })
    set_color("@type.qualifier", { fg = '#c678dd' })
    set_color("@type.builtin", { fg = '#c678dd' })

    set_color("@lsp.type.namespace", { fg = '#D18A66' })
    set_color("@lsp.mod.namespace", { fg = '#D18A66' })
    set_color("@lsp.type.enum", { fg = '#D19A66' })
    set_color("@lsp.type.enumMember", { fg = '#56B6C2' })
    set_color("@lsp.type.interface", { fg = '#98C379', italic=true })
    set_color("@lsp.type.parameter", { fg = '#ABB2BF', italic=true })
    set_color("@lsp.type.property", { fg = '#E06C75' })
    set_color("@lsp.type.selfKeyword", { fg = '#c678dd' })
    set_color("@lsp.type.selfTypeKeyword", { fg = '#c678dd' })
    set_color("@lsp.type.builtinType", { fg = '#c678dd' })
end

-- vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
-- vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
