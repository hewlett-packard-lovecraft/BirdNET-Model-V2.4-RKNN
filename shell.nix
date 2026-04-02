#!/usr/bin/env nix-shell
{
  pkgs ? import <nixpkgs> { },
}:
(
  let
    base = pkgs.appimageTools.defaultFhsEnvArgs;
  in
  pkgs.buildFHSEnv (
    base
    // {
      name = "FHS";
      targetPkgs =
        pkgs:
        (with pkgs; [
          gcc
          glibc
          zlib
          python311
          (python311.withPackages (
            python-pkgs: with python-pkgs; [
              pip
              virtualenv
              basedpyright
            ]
          ))
        ]);
      runScript = "zsh";
      extraOutputsToInstall = [ "dev" ];
    }
  )
).env
