{
  description = "Python dev flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin"];

    forEachSupportedSystem = f:
      nixpkgs.lib.genAttrs supportedSystems (system:
        f {
          pkgs = import nixpkgs {inherit system;};
        });
  in {
    devShells = forEachSupportedSystem ({pkgs}: {
      default = pkgs.mkShell {
        packages = with pkgs; [
          python313
          uv
          # python313Packages.numpy

          # stdenv.cc.cc.lib
        ];

        env = {
          UV_PYTHON = "${pkgs.python313}/bin/python";
          UV_PYTHON_DOWNLOADS = "never";

          # LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH";
        };

        shellHook = ''
        '';
      };
    });
  };
}
