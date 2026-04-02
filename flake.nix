{
  description = "RKNN-Toolkit2";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      base = pkgs.appimageTools.defaultFhsEnvArgs;
    in
    {
      devShells.x86_64-linux.default = pkgs.buildFHSEnv (
        base
        // {
          name = "FHS";
          targetPkgs =
            pkgs:
            (with pkgs; [
              gcc
              glibc
              zlib
              python312
              (python312.withPackages (
                python-pkgs: with python-pkgs; [
                  pip
                  virtualenv
                  basedpyright
                  #ruff
                ]
              ))
            ]);
          runScript = "zsh";
          extraOutputsToInstall = [ "dev" ];
          # postInstall = ''
          #   if [ ! -d ".venv" ]; then
          #     python3 -m venv .venv
          #   fi

          #   source .venv/bin/activate
          #   pip install -r requirements.txt
          # '';
        }
      );
    };
}
