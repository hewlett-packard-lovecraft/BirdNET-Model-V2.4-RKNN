# shell.nix
let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {

  packages = [
    pkgs.ty

    (pkgs.python3.withPackages (
      python-pkgs: with python-pkgs; [

        # select Python packages here
        pandas
        requests

        numpy
        librosa
        onnx
        onnxruntime
        sounddevice
        soundfile
        tensorflow

        onnxslim
        onnxconverter-common
        onnxmltools
        onnxruntime
        onnxruntime-tools
        sympy

      ]
    ))

  ];
}
