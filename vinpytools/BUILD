load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "generator",
    srcs = ["generator.py"],
    visibility = ["//visibility:public"],
    deps = [":iterator"],
)

py_library(
    name = "iterator",
    srcs = ["iterator.py"],
    visibility = ["//visibility:public"],
)
