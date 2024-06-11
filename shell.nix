{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell
{
  nativeBuildInputs = with pkgs; [
    nodejs
    python312
    poetry
  ];
}
