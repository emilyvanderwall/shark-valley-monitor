2026-07-26T19:22:23.5926393Z Current runner version: '2.335.1'
2026-07-26T19:22:23.5944886Z ##[group]Runner Image Provisioner
2026-07-26T19:22:23.5945698Z Hosted Compute Agent
2026-07-26T19:22:23.5946286Z Version: 20260707.563
2026-07-26T19:22:23.5946974Z Commit: 02667638d2b423fbc733a8e32a88b44996a3ba6e
2026-07-26T19:22:23.5947720Z Build Date: 2026-07-07T19:33:50Z
2026-07-26T19:22:23.5948460Z Worker ID: {a13114a9-cb57-44fc-af8a-b9d6f9867f92}
2026-07-26T19:22:23.5949175Z Azure Region: westus3
2026-07-26T19:22:23.5949738Z ##[endgroup]
2026-07-26T19:22:23.5951052Z ##[group]Operating System
2026-07-26T19:22:23.5951685Z Ubuntu
2026-07-26T19:22:23.5952401Z 24.04.4
2026-07-26T19:22:23.5952962Z LTS
2026-07-26T19:22:23.5953483Z ##[endgroup]
2026-07-26T19:22:23.5954077Z ##[group]Runner Image
2026-07-26T19:22:23.5954671Z Image: ubuntu-24.04
2026-07-26T19:22:23.5955204Z Version: 20260720.247.2
2026-07-26T19:22:23.5956435Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260720.247/images/ubuntu/Ubuntu2404-Readme.md
2026-07-26T19:22:23.5957931Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260720.247
2026-07-26T19:22:23.5958896Z ##[endgroup]
2026-07-26T19:22:23.5960103Z ##[group]GITHUB_TOKEN Permissions
2026-07-26T19:22:23.5961977Z Contents: read
2026-07-26T19:22:23.5962714Z Metadata: read
2026-07-26T19:22:23.5963384Z Packages: read
2026-07-26T19:22:23.5963925Z ##[endgroup]
2026-07-26T19:22:23.5966181Z Secret source: Actions
2026-07-26T19:22:23.5966881Z Prepare workflow directory
2026-07-26T19:22:23.6222895Z Prepare all required actions
2026-07-26T19:22:23.6254888Z Getting action download info
2026-07-26T19:22:23.9076014Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-07-26T19:22:24.6907834Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-07-26T19:22:24.8334628Z Complete job name: test
2026-07-26T19:22:24.8915397Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-07-26T19:22:24.8924040Z ##[group]Run actions/checkout@v4
2026-07-26T19:22:24.8924902Z with:
2026-07-26T19:22:24.8925459Z   repository: emilyvanderwall/shark-valley-monitor
2026-07-26T19:22:24.8929381Z   token: ***
2026-07-26T19:22:24.8929902Z   ssh-strict: true
2026-07-26T19:22:24.8930393Z   ssh-user: git
2026-07-26T19:22:24.8930920Z   persist-credentials: true
2026-07-26T19:22:24.8931455Z   clean: true
2026-07-26T19:22:24.8931974Z   sparse-checkout-cone-mode: true
2026-07-26T19:22:24.8932699Z   fetch-depth: 1
2026-07-26T19:22:24.8933185Z   fetch-tags: false
2026-07-26T19:22:24.8933739Z   show-progress: true
2026-07-26T19:22:24.8934240Z   lfs: false
2026-07-26T19:22:24.8934826Z   submodules: false
2026-07-26T19:22:24.8935321Z   set-safe-directory: true
2026-07-26T19:22:24.8935887Z   allow-unsafe-pr-checkout: false
2026-07-26T19:22:24.8936619Z ##[endgroup]
2026-07-26T19:22:24.9789889Z Syncing repository: emilyvanderwall/shark-valley-monitor
2026-07-26T19:22:24.9792707Z ##[group]Getting Git version info
2026-07-26T19:22:24.9793592Z Working directory is '/home/runner/work/shark-valley-monitor/shark-valley-monitor'
2026-07-26T19:22:24.9795144Z [command]/usr/bin/git version
2026-07-26T19:22:24.9830020Z git version 2.54.0
2026-07-26T19:22:24.9846928Z ##[endgroup]
2026-07-26T19:22:24.9858886Z Temporarily overriding HOME='/home/runner/work/_temp/24972159-b64f-4c81-a231-3625a93f621a' before making global git config changes
2026-07-26T19:22:24.9860803Z Adding repository directory to the temporary git global config as a safe directory
2026-07-26T19:22:24.9863833Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/shark-valley-monitor/shark-valley-monitor
2026-07-26T19:22:24.9894586Z Deleting the contents of '/home/runner/work/shark-valley-monitor/shark-valley-monitor'
2026-07-26T19:22:24.9898113Z ##[group]Initializing the repository
2026-07-26T19:22:24.9903118Z [command]/usr/bin/git init /home/runner/work/shark-valley-monitor/shark-valley-monitor
2026-07-26T19:22:24.9997819Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-07-26T19:22:24.9999836Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-07-26T19:22:25.0001621Z hint: to use in all of your new repositories, which will suppress this warning,
2026-07-26T19:22:25.0003462Z hint: call:
2026-07-26T19:22:25.0004559Z hint:
2026-07-26T19:22:25.0005679Z hint: 	git config --global init.defaultBranch <name>
2026-07-26T19:22:25.0006975Z hint:
2026-07-26T19:22:25.0008316Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-07-26T19:22:25.0010057Z hint: 'development'. The just-created branch can be renamed via this command:
2026-07-26T19:22:25.0011554Z hint:
2026-07-26T19:22:25.0013068Z hint: 	git branch -m <name>
2026-07-26T19:22:25.0014240Z hint:
2026-07-26T19:22:25.0015502Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-07-26T19:22:25.0017711Z Initialized empty Git repository in /home/runner/work/shark-valley-monitor/shark-valley-monitor/.git/
2026-07-26T19:22:25.0021520Z [command]/usr/bin/git remote add origin https://github.com/emilyvanderwall/shark-valley-monitor
2026-07-26T19:22:25.0067211Z ##[endgroup]
2026-07-26T19:22:25.0068560Z ##[group]Disabling automatic garbage collection
2026-07-26T19:22:25.0070734Z [command]/usr/bin/git config --local gc.auto 0
2026-07-26T19:22:25.0116214Z ##[endgroup]
2026-07-26T19:22:25.0117562Z ##[group]Setting up auth
2026-07-26T19:22:25.0121271Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-07-26T19:22:25.0147454Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-07-26T19:22:25.0390390Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-07-26T19:22:25.0416538Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-07-26T19:22:25.0585892Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-07-26T19:22:25.0610666Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-07-26T19:22:25.0767655Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-07-26T19:22:25.0793002Z ##[endgroup]
2026-07-26T19:22:25.0794499Z ##[group]Fetching the repository
2026-07-26T19:22:25.0800807Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +7ee937e824d9fa6b6dd390061e126b7e0d44a71c:refs/remotes/origin/main
2026-07-26T19:22:25.3977968Z From https://github.com/emilyvanderwall/shark-valley-monitor
2026-07-26T19:22:25.3995013Z  * [new ref]         7ee937e824d9fa6b6dd390061e126b7e0d44a71c -> origin/main
2026-07-26T19:22:25.3997483Z ##[endgroup]
2026-07-26T19:22:25.3998642Z ##[group]Determining the checkout info
2026-07-26T19:22:25.4000030Z ##[endgroup]
2026-07-26T19:22:25.4003644Z [command]/usr/bin/git sparse-checkout disable
2026-07-26T19:22:25.4035612Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-07-26T19:22:25.4056590Z ##[group]Checking out the ref
2026-07-26T19:22:25.4060050Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-07-26T19:22:25.4089933Z Switched to a new branch 'main'
2026-07-26T19:22:25.4091821Z branch 'main' set up to track 'origin/main'.
2026-07-26T19:22:25.4097200Z ##[endgroup]
2026-07-26T19:22:25.4126195Z [command]/usr/bin/git log -1 --format=%H
2026-07-26T19:22:25.4152770Z 7ee937e824d9fa6b6dd390061e126b7e0d44a71c
2026-07-26T19:22:25.4371878Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-07-26T19:22:25.4375022Z ##[group]Run actions/setup-python@v5
2026-07-26T19:22:25.4375583Z with:
2026-07-26T19:22:25.4376020Z   python-version: 3.12
2026-07-26T19:22:25.4376567Z   check-latest: false
2026-07-26T19:22:25.4380113Z   token: ***
2026-07-26T19:22:25.4380610Z   update-environment: true
2026-07-26T19:22:25.4381123Z   allow-prereleases: false
2026-07-26T19:22:25.4381629Z   freethreaded: false
2026-07-26T19:22:25.4382313Z ##[endgroup]
2026-07-26T19:22:25.5555043Z ##[group]Installed versions
2026-07-26T19:22:25.5635456Z (node:2026) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-07-26T19:22:25.5637184Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-26T19:22:25.5638337Z Successfully set up CPython (3.12.13)
2026-07-26T19:22:25.5639676Z ##[endgroup]
2026-07-26T19:22:25.5830399Z ##[group]Run pip install -r requirements.txt
2026-07-26T19:22:25.5831333Z [36;1mpip install -r requirements.txt[0m
2026-07-26T19:22:25.5940109Z shell: /usr/bin/bash -e {0}
2026-07-26T19:22:25.5940883Z env:
2026-07-26T19:22:25.5941671Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:25.5942682Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib/pkgconfig
2026-07-26T19:22:25.5943460Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:25.5944141Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:25.5944795Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:25.5945478Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib
2026-07-26T19:22:25.5946076Z ##[endgroup]
2026-07-26T19:22:28.4340525Z Collecting requests (from -r requirements.txt (line 1))
2026-07-26T19:22:28.5110038Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-07-26T19:22:28.5497724Z Collecting playwright (from -r requirements.txt (line 2))
2026-07-26T19:22:28.5592763Z   Downloading playwright-1.61.0-py3-none-manylinux1_x86_64.whl.metadata (3.3 kB)
2026-07-26T19:22:28.6601514Z Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 1))
2026-07-26T19:22:28.6699674Z   Downloading charset_normalizer-3.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (41 kB)
2026-07-26T19:22:28.6996966Z Collecting idna<4,>=2.5 (from requests->-r requirements.txt (line 1))
2026-07-26T19:22:28.7092734Z   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
2026-07-26T19:22:28.7312952Z Collecting urllib3<3,>=1.26 (from requests->-r requirements.txt (line 1))
2026-07-26T19:22:28.7407339Z   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
2026-07-26T19:22:28.7606905Z Collecting certifi>=2023.5.7 (from requests->-r requirements.txt (line 1))
2026-07-26T19:22:28.7701823Z   Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
2026-07-26T19:22:28.8014410Z Collecting pyee<14,>=13 (from playwright->-r requirements.txt (line 2))
2026-07-26T19:22:28.8113920Z   Downloading pyee-13.0.1-py3-none-any.whl.metadata (3.0 kB)
2026-07-26T19:22:28.9188205Z Collecting greenlet<4.0.0,>=3.1.1 (from playwright->-r requirements.txt (line 2))
2026-07-26T19:22:28.9291022Z   Downloading greenlet-3.5.4-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
2026-07-26T19:22:28.9517501Z Collecting typing-extensions (from pyee<14,>=13->playwright->-r requirements.txt (line 2))
2026-07-26T19:22:28.9619698Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-07-26T19:22:28.9766126Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-07-26T19:22:29.0004383Z Downloading charset_normalizer-3.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (224 kB)
2026-07-26T19:22:29.0332426Z Downloading idna-3.18-py3-none-any.whl (65 kB)
2026-07-26T19:22:29.0555693Z Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
2026-07-26T19:22:29.0787440Z Downloading playwright-1.61.0-py3-none-manylinux1_x86_64.whl (47.4 MB)
2026-07-26T19:22:29.9065666Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.4/47.4 MB 58.7 MB/s  0:00:00
2026-07-26T19:22:29.9166067Z Downloading greenlet-3.5.4-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (621 kB)
2026-07-26T19:22:29.9219241Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 621.5/621.5 kB 113.8 MB/s  0:00:00
2026-07-26T19:22:29.9317003Z Downloading pyee-13.0.1-py3-none-any.whl (15 kB)
2026-07-26T19:22:29.9431556Z Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
2026-07-26T19:22:29.9552514Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-07-26T19:22:30.0552849Z Installing collected packages: urllib3, typing-extensions, idna, greenlet, charset_normalizer, certifi, requests, pyee, playwright
2026-07-26T19:22:31.0339254Z 
2026-07-26T19:22:31.0351723Z Successfully installed certifi-2026.7.22 charset_normalizer-3.4.9 greenlet-3.5.4 idna-3.18 playwright-1.61.0 pyee-13.0.1 requests-2.34.2 typing-extensions-4.16.0 urllib3-2.7.0
2026-07-26T19:22:31.0943502Z ##[group]Run playwright install chromium
2026-07-26T19:22:31.0943947Z [36;1mplaywright install chromium[0m
2026-07-26T19:22:31.0974897Z shell: /usr/bin/bash -e {0}
2026-07-26T19:22:31.0975251Z env:
2026-07-26T19:22:31.0975672Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:31.0976186Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib/pkgconfig
2026-07-26T19:22:31.0976674Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:31.0977131Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:31.0977606Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:31.0978116Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib
2026-07-26T19:22:31.0978532Z ##[endgroup]
2026-07-26T19:22:31.3914179Z Downloading Chrome for Testing 149.0.7827.55 (playwright chromium v1228) from https://cdn.playwright.dev/builds/cft/149.0.7827.55/linux64/chrome-linux64.zip
2026-07-26T19:22:32.3480334Z |                                                                                |   0% of 177 MiB
2026-07-26T19:22:32.4893930Z |■■■■■■■■                                                                        |  10% of 177 MiB
2026-07-26T19:22:32.5467835Z |■■■■■■■■■■■■■■■■                                                                |  20% of 177 MiB
2026-07-26T19:22:32.6125654Z |■■■■■■■■■■■■■■■■■■■■■■■■                                                        |  30% of 177 MiB
2026-07-26T19:22:32.6672057Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                                |  40% of 177 MiB
2026-07-26T19:22:32.7016932Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                        |  50% of 177 MiB
2026-07-26T19:22:32.7629505Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                |  60% of 177 MiB
2026-07-26T19:22:32.8063723Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                        |  70% of 177 MiB
2026-07-26T19:22:32.8611545Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                |  80% of 177 MiB
2026-07-26T19:22:32.9152667Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■        |  90% of 177 MiB
2026-07-26T19:22:32.9753453Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% of 177 MiB
2026-07-26T19:22:35.8323591Z Chrome for Testing 149.0.7827.55 (playwright chromium v1228) downloaded to /home/runner/.cache/ms-playwright/chromium-1228
2026-07-26T19:22:35.8326787Z Downloading FFmpeg (playwright ffmpeg v1011) from https://cdn.playwright.dev/dbazure/download/playwright/builds/ffmpeg/1011/ffmpeg-linux.zip
2026-07-26T19:22:36.9412941Z |                                                                                |   0% of 2.3 MiB
2026-07-26T19:22:36.9657637Z |■■■■■■■■                                                                        |  10% of 2.3 MiB
2026-07-26T19:22:36.9780203Z |■■■■■■■■■■■■■■■■                                                                |  20% of 2.3 MiB
2026-07-26T19:22:36.9865913Z |■■■■■■■■■■■■■■■■■■■■■■■■                                                        |  30% of 2.3 MiB
2026-07-26T19:22:36.9947828Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                                |  40% of 2.3 MiB
2026-07-26T19:22:37.0004982Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                        |  50% of 2.3 MiB
2026-07-26T19:22:37.0021594Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                |  60% of 2.3 MiB
2026-07-26T19:22:37.0040094Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                        |  70% of 2.3 MiB
2026-07-26T19:22:37.0096690Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                |  80% of 2.3 MiB
2026-07-26T19:22:37.0120406Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■        |  90% of 2.3 MiB
2026-07-26T19:22:37.0130784Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% of 2.3 MiB
2026-07-26T19:22:37.0629779Z FFmpeg (playwright ffmpeg v1011) downloaded to /home/runner/.cache/ms-playwright/ffmpeg-1011
2026-07-26T19:22:37.0633043Z Downloading Chrome Headless Shell 149.0.7827.55 (playwright chromium-headless-shell v1228) from https://cdn.playwright.dev/builds/cft/149.0.7827.55/linux64/chrome-headless-shell-linux64.zip
2026-07-26T19:22:38.3169837Z |                                                                                |   0% of 114.2 MiB
2026-07-26T19:22:38.4645602Z |■■■■■■■■                                                                        |  10% of 114.2 MiB
2026-07-26T19:22:38.5411836Z |■■■■■■■■■■■■■■■■                                                                |  20% of 114.2 MiB
2026-07-26T19:22:38.5904795Z |■■■■■■■■■■■■■■■■■■■■■■■■                                                        |  30% of 114.2 MiB
2026-07-26T19:22:38.6382454Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                                |  40% of 114.2 MiB
2026-07-26T19:22:38.6711218Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                        |  50% of 114.2 MiB
2026-07-26T19:22:38.6980637Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                |  60% of 114.2 MiB
2026-07-26T19:22:38.7397968Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                        |  70% of 114.2 MiB
2026-07-26T19:22:38.7662263Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                |  80% of 114.2 MiB
2026-07-26T19:22:38.8099138Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■        |  90% of 114.2 MiB
2026-07-26T19:22:38.8339579Z |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% of 114.2 MiB
2026-07-26T19:22:40.9073196Z Chrome Headless Shell 149.0.7827.55 (playwright chromium-headless-shell v1228) downloaded to /home/runner/.cache/ms-playwright/chromium_headless_shell-1228
2026-07-26T19:22:40.9293193Z ##[group]Run python check.py
2026-07-26T19:22:40.9293535Z [36;1mpython check.py[0m
2026-07-26T19:22:40.9318789Z shell: /usr/bin/bash -e {0}
2026-07-26T19:22:40.9319183Z env:
2026-07-26T19:22:40.9319507Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:40.9319964Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib/pkgconfig
2026-07-26T19:22:40.9320401Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:40.9320784Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:40.9321180Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
2026-07-26T19:22:40.9321629Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib
2026-07-26T19:22:40.9322833Z   DISCORD_WEBHOOK: ***
2026-07-26T19:22:40.9323114Z ##[endgroup]
2026-07-26T19:23:04.2800058Z Number of events: 0
2026-07-26T19:23:04.3087191Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-07-26T19:23:04.3088167Z Post job cleanup.
2026-07-26T19:23:04.4100882Z (node:2188) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-07-26T19:23:04.4102496Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-26T19:23:04.4225640Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-07-26T19:23:04.4226664Z Post job cleanup.
2026-07-26T19:23:04.4960432Z [command]/usr/bin/git version
2026-07-26T19:23:04.4990863Z git version 2.54.0
2026-07-26T19:23:04.5019345Z Temporarily overriding HOME='/home/runner/work/_temp/8b5f7e9b-3891-464a-831b-bc642b80f3fd' before making global git config changes
2026-07-26T19:23:04.5020537Z Adding repository directory to the temporary git global config as a safe directory
2026-07-26T19:23:04.5024452Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/shark-valley-monitor/shark-valley-monitor
2026-07-26T19:23:04.5055542Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-07-26T19:23:04.5085604Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-07-26T19:23:04.5268445Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-07-26T19:23:04.5290578Z http.https://github.com/.extraheader
2026-07-26T19:23:04.5299854Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-07-26T19:23:04.5328314Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-07-26T19:23:04.5497309Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-07-26T19:23:04.5520970Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-07-26T19:23:04.5832539Z Cleaning up orphan processes
2026-07-26T19:23:04.5980334Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
