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

# 必要に応じてビルド設定を追加
set_target_properties(IntegratedExecutable PROPERTIES
    CXX_STANDARD 14
)
