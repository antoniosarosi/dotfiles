require("nvim-web-devicons").setup {
    strict = true,
    override_by_filename = {
        [".gitignore"] = {
            icon = "",
            color = "#f1502f",
            name = "Gitignore"
        },
        ["go.mod"] = {
            icon = "󰟓",
            color = "#ec407a",
            name = "GoMod",
        }
    },
}
