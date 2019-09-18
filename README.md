# Raspberry-pi-Car
Use Raspberry pi to make a car



mkdir -p Bin/Intermediate/Arm-Release/SimpleViewer
g++ -MD -MP -MT "./Bin/Intermediate/Arm-Release/SimpleViewer/Viewer.d Bin/Intermediate/Arm-Release/SimpleViewer/Viewer.o" -c -march=armv7-a -mtune=cortex-a9 -mfpu=neon -mfloat-abi=hard  -O3 -fno-tree-pre -fno-strict-aliasing -ftree-vectorize -ffast-math -funsafe-math-optimizations  -flax-vector-conversions -DUNIX -DGLX_GLXEXT_LEGACY -Wall -O2 -DNDEBUG -I../../Include -I../../ThirdParty/GL/ -I../Common -I/home/pi/aobi/OpenNI_2.3.0.63/Linux/OpenNI-Linux-Arm-2.3.0.63/Include -DXN_NEON -fPIC -fvisibility=hidden -Werror -o Bin/Intermediate/Arm-Release/SimpleViewer/Viewer.o Viewer.cpp
Viewer.cpp: In constructor ‘SampleViewer::SampleViewer(const char*, openni::Device&, openni::VideoStream&, openni::VideoStream&)’:
Viewer.cpp:70:9: error: ‘char* strncpy(char*, const char*, size_t)’ specified bound 256 equals destination size [-Werror=stringop-truncation]
  strncpy(m_strSampleName, strSampleName, ONI_MAX_STR);
  ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make: *** [CommonCppMakefile:133: Bin/Intermediate/Arm-Release/SimpleViewer/Viewer.o] Error 1
