cmake_minimum_required(VERSION 3.14)

# プロジェクト名の設定
project(IntegratedProject)

# サブモジュールのパスを記述した設定ファイルを読み込む
set(SUBMODULES_FILE "${CMAKE_SOURCE_DIR}/submodules.txt")

# 設定ファイルが存在するか確認
if(EXISTS ${SUBMODULES_FILE})
    file(READ ${SUBMODULES_FILE} SUBMODULES_CONTENT)
    string(REPLACE "\n" ";" SUBMODULES_LIST "${SUBMODULES_CONTENT}")
else()
    message(FATAL_ERROR "Submodule configuration file not found: ${SUBMODULES_FILE}")
endif()

# サブモジュールを動的に追加
foreach(submodule_info IN LISTS SUBMODULES_LIST)
    string(REGEX MATCH "^(.*)=(.*)$" matched ${submodule_info})
    if(matched)
        set(submodule_name ${CMAKE_MATCH_1})
        set(submodule_path ${CMAKE_MATCH_2})
        message(STATUS "Adding submodule: ${submodule_name} at ${submodule_path}")
        add_subdirectory(${submodule_path})
    endif()
endforeach()

# 出力ディレクトリの設定（オプション）
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/build)

# 統合用のターゲットを作成（例: 実行ファイル）
add_executable(IntegratedExecutable main.cpp)

# 他のリポジトリのライブラリやターゲットをリンク
target_link_libraries(IntegratedExecutable
    repository1_library
    repository2_library
    repository3_library
)

# コンパイル対象ファイルを静的解析の実行用にかき集めてくるフォルダを生成
set(COMPILE_DIR ${CMAKE_BINARY_DIR}/compile_sources)
file(MAKE_DIRECTORY ${COMPILE_DIR})

# ソースファイルを集める
foreach(SRC_FILE ${SOURCE_FILES})
    get_filename_component(FILE_NAME ${SRC_FILE} NAME)
    configure_file(${SRC_FILE} ${COMPILE_DIR}/${FILE_NAME} COPYONLY)
endforeach()

# 必要に応じてビルド設定を追加
set_target_properties(IntegratedExecutable PROPERTIES
    CXX_STANDARD 14
)
