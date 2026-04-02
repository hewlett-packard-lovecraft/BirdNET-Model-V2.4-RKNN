{
  lib,
  buildPythonPackage,
  fetchPypi,
  setuptools,
  wheel,
}:

buildPythonPackage rec {
  pname = "rknn-toolkit2";
  version = "2.3.2";
  src = fetchPypi {
    inherit pname version;
    hash = "sha256-d78e2ecd77502988dc2dcd46d665102be8fb15f4d4d541ef272f6abaabca0eda=";
  };

  # do not run tests

  doCheck = false;

  # specific to buildPythonPackage, see its reference

  pyproject = true;

  build-system = [
    setuptools
    wheel

  ];
}
