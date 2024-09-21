load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "be04b635c7be4604be1ef20542e9870af3c49778ce841ee2d92fcb42f9d9516a",
    strip_prefix = "rules_python-0.35.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.35.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python311",
    python_version = "3.11",
)

load("@python311//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "deps",
    # enable_implicit_namespace_pkgs = True,
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements.lock",
)

load("@deps//:requirements.bzl", "install_deps")

install_deps()
