#  Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных формате .txt.
import controller as contr
import user_interface as ui
import importTXT as itxt
import exportTXT as exptxt

itxt.database_creator(itxt.file_name)
contr.to_do(ui.action)
exptxt.data_export(exptxt.file_name)