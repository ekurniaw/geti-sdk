# v1.8.0 Intel® Geti™ SDK (06-09-2023)
## What's Changed
* Predict video on local by @jihyeonyi in https://github.com/openvinotoolkit/geti-sdk/pull/243
* Update job datamodel for new job scheduler by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/251
* Add `model` key to TestMetaData by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/252
* Improve error handling for version parsing by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/253
* Update SECURITY.md by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/256
* Add `nosec` for safe subprocess use in `predict_video.py` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/257
* Update openvino to 2023.0 and OTX to v1.4 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/255
* Update opencv-python requirement from ==4.5.* to ==4.8.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/249
* Bump orjson from 3.8.8 to 3.9.2 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/250
* Enable using pre-production dependencies in test builds by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/258
* Update the list of third party programs by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/259
* Require `cryptography>=41.0.2` for security reasons by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/260
* Fix for responding to Project Key values in the REST API by @harimkang in https://github.com/openvinotoolkit/geti-sdk/pull/264
* Disable parallel execution on pre-merge tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/270
* Fix model_api import and model creation for deployments by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/268
* CVS-116946 Make platform version parsing robust by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/269
* Update Performance attribute interfaces by @harimkang in https://github.com/openvinotoolkit/geti-sdk/pull/271
* CVS-118292 Update ATSS algo name by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/272
* Fix deployment postprocessing by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/273

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.8...v.1.8.0

# v1.5.8 Intel® Geti™ SDK (19-06-2023)
## What's Changed
* Update vcrpy requirement from ==4.2.* to ==4.3.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/227
* Specify correct project name in notebook 009 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/229
* Fix name of project to download in notebook 009 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/233
* Update pytest-cov requirement from ==4.0.* to ==4.1.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/231
* upgrate isort to 5.12.0 to avoid runtime error in pre-commit in python 3.8 by @jihyeonyi in https://github.com/openvinotoolkit/geti-sdk/pull/235
* Update all pre-commit hooks to latest versions by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/237
* Add `step_size` field to configurable floats by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/241
* Handle re-authentication during media upload robustly by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/244

## New Contributors
* @jihyeonyi made their first contribution in https://github.com/openvinotoolkit/geti-sdk/pull/235

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.7...v1.5.8

# v1.5.7 Intel® Geti™ SDK (30-05-2023)
## What's Changed
* Allow more efficient image uploading for datumaro annotation readers by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/224
* Fix deployment for `otx v1.2.2` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/225


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.6...v1.5.7

# v1.5.6 Intel® Geti™ SDK (23-05-2023)
## What's Changed
* Add `group` key to hierarchical label definition in notebook 001 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/220
* Add `TestingClient` to perform model tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/221
* Wait for a project to become ready after it is created by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/223
* Update requests requirement from ==2.28.* to ==2.31.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/222


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.5...v1.5.6

# v1.5.5 Intel® Geti™ SDK (15-05-2023)
## What's Changed
* Add param to disable certificate validation for data download helpers by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/218


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.4...v1.5.5

# v1.5.4 Intel® Geti™ SDK (11-05-2023)
## What's Changed
* Add active learning client for retrieving the active set by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/215
* Allow passing label dictionaries to `Geti.create_single_task_project_from_dataset` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/216
* Add string representation for `GetiVersion` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/217


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.3...v1.5.4

# v1.5.3 Intel® Geti™ SDK (10-05-2023)
## What's Changed
* Add `ONNX` as optimization type by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/212
* Remove trailing slash from the base url in the media rest client by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/214
* Update pytest requirement from ==7.2.* to ==7.3.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/211
* Fix nightly tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/213


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.2...v1.5.3

# v1.5.2 Intel® Geti™ SDK (08-05-2023)
## What's Changed
* Add score NoneType check in summary function of ProjectStatus by @harimkang in https://github.com/openvinotoolkit/geti-sdk/pull/208
* Update `OptimizedModel` data model by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/209
* Update datumaro requirement from ==1.1.* to ==1.2.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/206

## New Contributors
* @harimkang made their first contribution in https://github.com/openvinotoolkit/geti-sdk/pull/208

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.1...v1.5.2

# v1.5.1 Intel® Geti™ SDK (26-04-2023)
## What's Changed
* Update hashing algorithm to `sha3_512` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/204
* Bump otx from 1.1.2 to 1.2.0 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/203
* Update ipython requirement from ==8.11.* to ==8.12.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/202


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.5.0...v1.5.1

# v1.5.0 Intel® Geti™ SDK (24-04-2023)
## What's Changed
* Pin orjson version to 3.8.8 to avoid installation error by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/178
* Fix nightly tests for classification project by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/179
* Add workaround to set output blob name if not set by model adapter by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/180
* Add workflow to publish to TestPyPI by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/185
* Filter on polygons when setting Datum segmentation dataset by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/184
* Add `explain` method for deployment by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/183
* Remove duplicate annotations for datumaro dataset items by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/186
* Remove specific geti version tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/187
* Add python version compatibility table to README by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/189
* Add test for python 3.10 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/188
* Use absolute URLs for links in readme by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/190
* Fix explain for segmentation and anomaly models by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/191
* Replace the deprecated `DatasetItem.image()` in DatumAnnotationReader by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/192
* Update datumaro requirement from ==1.0.* to ==1.1.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/175
* Update pillow requirement from ==9.4.* to ==9.5.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/182
* Pagination for project fetching by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/197
* Use pagination when fetching all the projects by @leoll2 in https://github.com/openvinotoolkit/geti-sdk/pull/193
* Fix dataset filtering issue for Datumaro annotation reader by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/194
* Update simplejson requirement from ==3.18.* to ==3.19.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/196
* Bump otx from 1.1.0 to 1.1.2 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/195
* Update omegaconf requirement from ==2.1.* to ==2.3.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/120
* Add finalizer to remove demo project after nightly test by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/198
* Add support for additional datasets in project by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/199

## New Contributors
* @leoll2 made their first contribution in https://github.com/openvinotoolkit/geti-sdk/pull/193

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.4.1...v1.5.0

# [Pre-release] v1.4.1 Intel® Geti™ SDK (28-03-2023)
## What's Changed
* Update otx requirement to `otx==1.1.0` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/176
* Make model wrapper module namespace unique by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/177


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.4.0...v1.4.1

# [Pre-release] v1.4.0 Intel® Geti™ SDK (27-03-2023)
## What's Changed
* Migrate from `ote_sdk` to `otx.api` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/166

## Caution: Backwards incompatibility for project `Deployments`
This release breaks backwards compatibility with `deployments` created by earlier versions of the Intel® Geti™ platform. Please only update to this version of the Geti SDK if you are sure that your Intel® Geti™ server is also on version 1.4 or later.

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.2.4...v1.4.0

# v1.2.4 Intel® Geti™ SDK (27-03-2023)
## What's Changed
* Update ipython requirement from ==8.10.* to ==8.11.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/172
* Fix `upload_and_predict_from_numpy.py` example by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/173
* Improve error handling for OVMS deployment by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/174


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.2.3...v1.2.4

# v1.2.3 Intel® Geti™ SDK (13-03-2023)
## What's Changed
* Fix saving images and annotations with non-ascii characters in their filename by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/160
* Update tqdm requirement from ==4.64.* to ==4.65.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/161
* Cvs-96625 Update image display method in `show_image_with_annotation_scene` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/164
* Enable uploading data from nested subsets in DatumAnnotationReader by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/163
* Update datumaro requirement from ==0.4.* to ==1.0.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/155
* Update OptimizedModel and TaskStatus data models by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/165
* Formatting images and cell - Notebook 102 suggestions by @paularamo in https://github.com/openvinotoolkit/geti-sdk/pull/167
* Add notebook `102_from_zero_to_hero` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/159
* Demo Zero to Hero in 9 steps by @paularamo in https://github.com/openvinotoolkit/geti-sdk/pull/154
* Fix deployment saving mechanism and handle errors by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/170
* Add ovmsclient to base requirements by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/169
* Issue 168: Fix tempdir cleanup in `DeployedModel` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/171

## New Contributors
* @paularamo made their first contribution in https://github.com/openvinotoolkit/geti-sdk/pull/167

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.2.2...v1.2.3

# v1.2.2 Intel® Geti™ SDK (28-02-2023)
## What's Changed
* Enable OVMS deployment by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/148
* Minor fixes for notebook 010 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/149
* Update ipython requirement from ==8.9.* to ==8.10.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/151
* Add performance hint to the ovms config by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/152
* Fix bug in deployment resource clean up method by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/153
* Update python-dotenv requirement from ==0.21.* to ==1.0.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/156
* Add a short sleep in `Geti.upload_project` after media upload by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/157
* Add OVMS deployment resources to manifest by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/158


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.2.1...v1.2.2

# v1.2.1 Intel® Geti™ SDK (02-02-2023)
## What's Changed
* Fix issue with deployment for anomaly classification models by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/144
* Require `mistune>=2.0.3` for notebooks by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/147
* Update ipython requirement from ==8.8.* to ==8.9.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/145
* Fix issue with temporary resource clean up for `Deployment`s by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/146


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.2.0...v1.2.1

# v1.2 Intel® Geti™ SDK (24-01-2023)
## What's Changed
* Add `size` field to MediaInformation data model by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/133
* Update available Geti versions by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/134
* Update pillow requirement from ==9.3.* to ==9.4.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/131
* Fix a mismatch in the data model for the Optimization Job by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/136
* Add DeploymentClient to streamline deployment mechanism by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/135
* Update prediction mechanism by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/137
* Update ipython requirement from ==8.7.* to ==8.8.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/138
* Bump openvino from 2022.2.0 to 2022.3.0 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/130
* Update various dependencies by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/140
* Minor refactor in `Geti` class and fix in `predict_image` method by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/139
* Make `maps` key optional when converting Predictions from dictionary input by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/141
* Fix documentation workflow to deploy from build artifact by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/143
* Make workaround for issue with detection prediction conversion by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/142


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.1.1...v1.2.0

# v1.1.1 Intel® Geti™ SDK (20-12-2022)
## What's Changed
* Fix issue with model to dictionary conversion by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/128
* Only submit train request once all running jobs for task have finished by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/129


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.1.0...v1.1.1

# v1.1.0 Intel® Geti™ SDK (15-12-2022)
## What's Changed
* Minor fix in README.md by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/118
* Fix and improve geti version comparison mechanism by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/117
* Ignore some false positive bandit detections by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/119
* Update datumaro requirement from ==0.3.* to ==0.4.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/121
* Add ClamAV workflow by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/123
* Update `jupyterlab` requirement for notebooks to >=3.5.1 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/124
* Increase timeout for training job polling upon calling `train_task` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/125


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.0.4...v1.1.0

# v1.0.4 Intel® Geti™ SDK (08-12-2022)
## What's Changed
* Update ipython requirement from ==8.6.* to ==8.7.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/112
* Properly check for empty annotation before uploading by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/111
* Update numpy version to 1.22.* in requirements by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/104
* Minor update to README.md by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/114
* Update training client to handle new /train endpoint response by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/113
* Update `StatusSummary` datamodel by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/115


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.0.3...v1.0.4

# v1.0.3 Intel® Geti™ SDK (25-11-2022)
## What's Changed
* Add `ScoreMetadata` to represent the new `scores` field by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/106
* Add model and prediction client integration tests + update cassettes by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/107
* Update simplejson requirement from ==3.17.* to ==3.18.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/108
* Fix opencv window closure bug by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/109


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.0.2...v1.0.3

# v1.0.2 Intel® Geti™ SDK (17-11-2022)
## What's Changed
* Update ote-sdk requirement to v0.3.1 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/98
* Add integration tests for `project_client`, fix `project_client.add_labels` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/99
* Update data model for TaskMetadata, improve robustness of active model fetching by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/100
* Use OTE SDK visualizer, add plot helper unit tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/101
* Add HTTPS_PROXY as variable to the credentials helper by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/102
* Add tests for video up- and download in Geti integration tests by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/103


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.0.1...v1.0.2

# v1.0.1 Intel® Geti™ SDK (11-11-2022)
## What's Changed
* Add path validation to project download target path by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/87
* Update tqdm requirement from ==4.62.* to ==4.64.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/84
* Update python-dotenv requirement from ==0.20.* to ==0.21.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/86
* Add security note to README for project download by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/88
* Update numpy requirement to 1.21.* by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/89
* Reduce permissions upon directory creation by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/90
* Update README to correctly reference Intel Geti brand everywhere by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/92
* Improve check for video processing in `Geti.upload_project()` to avoid potential infinite loop by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/93
* Add unit tests to pre-merge test suite by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/91
* Update ProjectStatus and TaskStatus to include new field `n_new_annotations` by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/94
* Add progress bars for up/download of projects, media, annotations and predictions by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/95
* Add ipywidgets to notebook requirements by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/97


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v1.0.0...v1.0.1

# v1.0.0 Intel® Geti™ SDK (04-11-2022)
## What's Changed
* Add a re-authentication mechanism when using token authentication by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/72
* Update pytest requirement from ==7.1.* to ==7.2.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/73
* Update pillow requirement from ==9.2.* to ==9.3.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/74
* Update pytest-html requirement from ==3.1.* to ==3.2.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/75
* Catch value error when invalid datetime string is converted by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/76
* Update nightly test workflow to include tests against Geti `develop` branch by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/78
* Enable SSL certificate validation by default by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/77
* Remove disallowed fields from project before POSTing by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/79
* Ignore false positive bandit detections by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/80
* Update numpy, ipython, jupyterlab versions by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/81
* Fix and unify folder naming for project download by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/82


## Breaking Changes
* The `Geti` class now has SSL certificate validation enabled by default. This will result in an error when connecting to a server with a certificate that can't be validated. Note that it is still possible to disable certificate validation by passing `verify_certificate = False` when initializing the `Geti` instance. Please note that disabling certificate validation is unsafe and should only be considered in a secure network environment.


**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v0.2.4...v1.0.0rc1

# v0.2.4 Intel® Geti™ SDK (25-10-2022)
## What's Changed
* Auto detect normalized annotation files for GetiAnnotationReader by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/63
* Fix version detection mechanism and add tests for GetiVersion by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/64
* Minor changes for backward compatibility with SCv1.1 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/67
* Enable proxies in ONLINE test mode by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/66
* Fix proxy config in tests for online mode by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/68
* Updated Attrs Classes and Fields by @HiteshManglani123 in https://github.com/openvinotoolkit/geti-sdk/pull/65
* Validate media filename upon download by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/69
* Update pytest-env requirement from ==0.6.* to ==0.8.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/70
* Fix anomaly classification deployment by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/71

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v0.2.3...v0.2.4

# v0.2.3 Intel® Geti™ SDK (06-10-2022)
## What's Changed
* Remove VCR from nightly test for demos by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/54
* Improve nightly tests for `demos` module by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/55
* Update sc_annotation_reader by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/56
* Add version to optimized model by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/57
* Update SDK platform version parsing mechanism by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/58
* Add nightly tests against Geti-MVP by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/59
* Handle failed training jobs in notebook 007 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/60
* Update example script to store prediction results to file by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/61

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v0.2.2...v0.2.3

# v0.2.2 Intel® Geti™ SDK (04-10-2022)
## What's Changed
* Add coverage report to pre-merge and nightly test artifacts by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/47
* Correctly set permissions on extracted files for anomaly dataset by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/51
* Update pytest-cov requirement from ==3.0.* to ==4.0.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/50
* Update pillow requirement from ==9.1.* to ==9.2.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/48
* Workflow update: Run nightly and integration tests in one step and get coverage by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/53

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v0.2.1...v0.2.2

# v0.2.1 Intel® Geti™ SDK (30-09-2022)
## What's Changed
* Replace SC references in docstrings by Geti by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/33
* Change package name from `geti_sdk` to `geti-sdk`. Import names are unchanged by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/34
* Update vcrpy requirement from ==4.1.* to ==4.2.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/35
* Bump datumaro from 0.3 to 0.3.1 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/37
* Bump openvino from 2022.1.0 to 2022.2.0 in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/38
* Update requests requirement from ==2.26.* to ==2.28.* in /requirements by @dependabot in https://github.com/openvinotoolkit/geti-sdk/pull/39
* Handle exceptions in data deserialization by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/40
* Fix image path in notebook 008 by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/41
* Use personal access token instead of credential authentication by default by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/42
* Add image showing the personal access token menu to README by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/43
* Add nightly tests for `demos` module by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/44
* Add screenshot of jupyter lab landing page to README by @ljcornel in https://github.com/openvinotoolkit/geti-sdk/pull/45

## New Contributors
* @dependabot made their first contribution in https://github.com/openvinotoolkit/geti-sdk/pull/35

**Full Changelog**: https://github.com/openvinotoolkit/geti-sdk/compare/v0.2.0...v0.2.1

# v0.2.0 Intel® Geti™ SDK (27-09-2022)

This is the first official release of the Intel® Geti™ Software Development Kit (SDK).

The purpose of this SDK is twofold:

1. Provide an easy-to-use interface to the [Intel® Geti™ platform](www.geti.intel.com), to manipulate
Intel® Geti™ projects and other entities or automate tasks on the platform. All
of this from a Python script or Jupyter notebook.


2. Provide an API to deploy and run models trained on the Intel® Geti™ server on your local
machine. The SDK Deployment module provides a straightforward
route to create a deployment for your Intel® Geti™ project, save it to a local disk and run
it offline.

This SDK includes various example scripts and Jupyter notebooks which illustrate a
range of use cases for the SDK. Make sure to check them out if you're getting
started!
