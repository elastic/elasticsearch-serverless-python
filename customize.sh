#!/usr/bin/env bash

dir=$(dirname "$(realpath -s "$0")")

lang=$1
LANG="${lang^}"

# Update README.md
sed -i "s/<<\[lang\]>>/$lang/g" $dir/README_TEMPLATE.md
sed -i "s/<<\[LANG\]>>/$LANG/g" $dir/README_TEMPLATE.md

# CONTRIBUTING.md
sed -i "s/<<\[lang\]>>/$lang/g" $dir/CONTRIBUTING.md
sed -i "s/<<\[LANG\]>>/$LANG/g" $dir/CONTRIBUTING.md

# docs/getting-started.MDX
sed -i "s/<<\[lang\]>>/$lang/g" $dir/docs/getting-started.MDX
sed -i "s/<<\[LANG\]>>/$LANG/g" $dir/docs/getting-started.MDX

# docs/landing-page.MDX
sed -i "s/<<\[lang\]>>/$lang/g" $dir/docs/landing-page.MDX
sed -i "s/<<\[LANG\]>>/$LANG/g" $dir/docs/landing-page.MDX

# .github/workflows/test.yml
sed -i "s/<<\[lang\]>>/$lang/g" $dir/.github/workflows/tests.yml
sed -i "s/<<\[LANG\]>>/$LANG/g" $dir/.github/workflows/tests.yml

# Clean up
rm README.md
mv README_TEMPLATE.md README.md
rm customize.sh