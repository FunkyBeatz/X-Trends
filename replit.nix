{pkgs}: {
  deps = [
    pkgs.sudo
    pkgs.apt
    pkgs.geckodriver
    pkgs.glibcLocales
    pkgs.zlib
    pkgs.xcodebuild
  ];
}
