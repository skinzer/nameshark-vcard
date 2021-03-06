# nameshark-vcard
Converts vCards to the JSON format expected by the Name Shark app

[![GitHub tag](https://img.shields.io/github/tag/proinsias/nameshark-vcard.svg)]()
[![GitHub release](https://img.shields.io/github/release/proinsias/nameshark-vcard.svg)]()
[![GitHub forks](https://img.shields.io/github/forks/proinsias/nameshark-vcard.svg?style=social&label=Fork)]()
[![GitHub stars](https://img.shields.io/github/stars/proinsias/nameshark-vcard.svg?style=social&label=Star)]()
[![GitHub watchers](https://img.shields.io/github/watchers/proinsias/nameshark-vcard.svg?style=social&label=Watch)]()
[![GitHub followers](https://img.shields.io/github/followers/proinsias.svg?style=social&label=Follow)]()
[![GitHub issues](https://img.shields.io/github/issues/proinsias/nameshark-vcard.svg)]()
[![GitHub pull requests](https://img.shields.io/github/issues-pr/proinsias/nameshark-vcard.svg)]()
[![GitHub contributors](https://img.shields.io/github/contributors/proinsias/nameshark-vcard.svg)]()
[![license](https://img.shields.io/github/license/proinsias/nameshark-vcard.svg)]()

[![Travis Production Build](https://travis-ci.org/proinsias/nameshark-vcard.svg?branch=production)](https://travis-ci.org/proinsias/nameshark-vcard)
[![Travis Development Build](https://travis-ci.org/proinsias/nameshark-vcard.svg?branch=develop)](https://travis-ci.org/proinsias/nameshark-vcard)
[![Scrutinizer Production Build](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/build.png?b=production)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/build-status/production)
[![Scrutinizer Development Build](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/build.png?b=develop)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/build-status/develop)
[![AppVeyor Production Build](https://ci.appveyor.com/api/projects/status/0ta82u4piyao3ayg/branch/production?svg=true)](https://ci.appveyor.com/project/proinsias/nameshark-vcard)
[![AppVeyor Development Build](https://ci.appveyor.com/api/projects/status/0ta82u4piyao3ayg/branch/develop?svg=true)](https://ci.appveyor.com/project/proinsias/nameshark-vcard)

[![Codecov Production Coverage](https://codecov.io/gh/proinsias/nameshark-vcard/branch/production/graph/badge.svg)](https://codecov.io/gh/proinsias/nameshark-vcard)
[![Codecov Development Coverage](https://codecov.io/gh/proinsias/nameshark-vcard/branch/develop/graph/badge.svg)](https://codecov.io/gh/proinsias/nameshark-vcard)
[![Code Climate Coverage](https://codeclimate.com/github/proinsias/nameshark-vcard/badges/coverage.svg)](https://codeclimate.com/github/proinsias/nameshark-vcard/coverage)
[![Scrutinizer Production Coverage](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/coverage.png?b=production)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/?branch=production)
[![Scrutinizer Development Coverage](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/coverage.png?b=develop)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/?branch=develop)
[![Coveralls.io Production Coverage](https://coveralls.io/repos/github/proinsias/nameshark-vcard/badge.svg?branch=production)](https://coveralls.io/github/proinsias/nameshark-vcard?branch=production)
[![Coveralls.io Development Coverage](https://coveralls.io/repos/github/proinsias/nameshark-vcard/badge.svg?branch=develop)](https://coveralls.io/github/proinsias/nameshark-vcard?branch=develop)

[![Quantified Code](https://www.quantifiedcode.com/api/v1/project/3553d32e83a8475ea60237d6a02d7107/badge.svg)](https://www.quantifiedcode.com/app/project/3553d32e83a8475ea60237d6a02d7107)
[![Code Climate GPA](https://codeclimate.com/github/proinsias/nameshark-vcard/badges/gpa.svg)](https://codeclimate.com/github/proinsias/nameshark-vcard)
[![Code Climate Issue Count](https://codeclimate.com/github/proinsias/nameshark-vcard/badges/issue_count.svg)](https://codeclimate.com/github/proinsias/nameshark-vcard)
[![Codacy](https://api.codacy.com/project/badge/Grade/3d8c09af6ee6433eac751444665ce1e0)](https://www.codacy.com/app/francis-odonovan/nameshark-vcard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=proinsias/nameshark-vcard&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Production Code Quality](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/quality-score.png?b=production)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/?branch=production)
[![Scrutinizer Development Code Quality](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/badges/quality-score.png?b=develop)](https://scrutinizer-ci.com/g/proinsias/nameshark-vcard/?branch=develop)

[![ReviewNinja](https://app.review.ninja/57427690/badge)](https://app.review.ninja/proinsias/nameshark-vcard)

[![Requires Production](https://requires.io/github/proinsias/nameshark-vcard/requirements.svg?branch=production)](https://requires.io/github/proinsias/nameshark-vcard/requirements/?branch=production)
[![Requires Development](https://requires.io/github/proinsias/nameshark-vcard/requirements.svg?branch=develop)](https://requires.io/github/proinsias/nameshark-vcard/requirements/?branch=develop)
[![VersionEye](https://www.versioneye.com/user/projects/57244381ba37ce00350af8c3/badge.svg?style=flat)](https://www.versioneye.com/user/projects/57244381ba37ce00350af8c3)
[![Libraries.io releases](https://img.shields.io/librariesio/release/proinsias/nameshark-vcard/1.0.3.svg)]()
[![Libraries.io GitHub](https://img.shields.io/librariesio/github/proinsias/nameshark-vcard.svg)]()

As you can tell from the number of badges above, I'm using this toy
project to experiment with various services prior to deploying them in
my private repos. If you have a favorite service that I'm missing,
feel free to create an issue!

Branch Organization
------------

    ├── production        <- Production branch with full test set.
    ├── develop           <- Development branch with reduced test set.
    └── developer/change  <- Developer sandbox branches without testing.

* Python Versions Tested:
    - 2.7 (via Travis & AppVeyor)
    - 3.4 (via Travis & AppVeyor)
    - 3.5 (via Travis)
    - 3.5-dev (via Travis)
    - 3.6-dev (via Travis)
    - nightly (via Travis)
    - pypy (via Travis)
    - pypy3 (via Travis)
* Platforms Tested:
    - Ubuntu 12.04 LTS Server Edition 64 bit (via Travis)
    - x86 (via AppVeyor)
    - x64 (via AppVeyor)
