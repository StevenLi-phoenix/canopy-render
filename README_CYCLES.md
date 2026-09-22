# CANOPY / 高精度 Cycles

本版本使用 n8 的 RTX 4070 Ti SUPER 16 GB，通过 OptiX 渲染。输出为原生 3840 × 1608、24 fps、336 帧、14 秒。

## 画质设置

- Cycles 最高 512 采样，最低 64 采样，自适应噪声阈值 0.01。
- 最多 12 次光线反弹，其中体积散射最多 4 次。
- 体积步长系数 0.5，最多 4096 步。
- OpenImageDenoise，Accurate 预滤波。
- 16 位 RGB PNG 中间帧，运动模糊快门 0.18。
- 保留原始连续程序化烟雾材质。测试过体积网格优化，但由于细节变软，没有用于正式版本。

自适应采样会让已收敛的像素提前停止；512 是每像素的上限，并非保证每个像素都运行 512 次。

## 文件与状态

- `Canopy_Cycles.blend`：保存上述设置的可编辑场景，可立即打开。
- `Canopy_Cycles_Detail_Test.png`：512 采样的局部测试，非完整画面。
- `cycles_render_status.json`：远程作业状态、已完成帧数和当前阶段；以该文件确认是否完成。
- `cycles_render_validation.json`：渲染设置、发射时序，以及完成后的文件与视频检查结果。
- `Canopy_Cycles_Hero_3840x1608.png`：第 180 帧，原生 4K、16 位。
- `Canopy_Cycles_3840x1608_24fps.mp4`：便于播放的 H.264 成片。
- `Canopy_Cycles_3840x1608_24fps_ProRes.mov`：ProRes 422 HQ、10 位编辑母版。

影片和完整 Hero 静帧只会在相应渲染完成后出现。不要将局部测试图视作完成的整帧或成片。

## 编辑与重渲染

车辆、发射时序、摄影机及烟雾控制方式与 `README.md` 中的编辑说明相同；本版本以这里列出的 Cycles 设置为准。场景包含 144 台车、3,456 次发射，无外部图像或体积缓存依赖。

在 Blender 5.2.2 或兼容版本中打开场景，在 Preferences → System 中选择支持的 Cycles 设备，然后使用 Render Animation。随附 `render_scene.py` 同样可输出 PNG 序列；它使用场景保存的引擎设置，但将 PNG 输出设为 8 位。如需 16 位中间帧，请将脚本中的 `color_depth` 改为 `'16'`，或直接从 Blender 渲染。

n8 工作目录为 `/home/lishuyu/Codes/canopy-render`。正式序列在 `work/cycles_precision_frames/`；渲染日志为 `work/cycles_precision_full.log`。作业支持跳过已有完整 PNG 后继续计算。

n8 已配置完成后的帧校验、视频编码和解码检查。本机的后台同步程序每五分钟检查一次；本机保持运行并能连接 n8 时，会自动回传 Hero 静帧和最终文件。本机休眠期间 n8 的渲染不受影响，回传需待本机恢复运行。

高采样 Cycles 改善光线追踪、散射和噪点，不会自动把现有程序化烟雾变成流体模拟，也不会改变原场景的建模与材质细节上限。
