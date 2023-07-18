
# @classmethod
#     def delete_source(cls, old: str) -> None:
#         """
#         Delete sourse files and folders after copy (and accept warnings dialogs)
#         :param cls:
#         :param old: deleted items
#         :return:
#         """
#         msg_text = "Remove old data?\n" \
#                    f"If you press 'Yes' all you backup`s and settings data in \n {old} \nwill be " \
#                    "deleted."
#         reply = mw.msg_two_button("WARNING!", msg_text)
#         if reply == 'no':
#             return
#         else:
#             cls.del_item(old)
pass


# @classmethod
# def del_item_old(cls, item: str) -> None:
#     for _ in Path.iterdir(Path(item)):
#
#         if _.is_dir():
#             try:
#                 shutil.rmtree(_, ignore_errors=False, onerror=cls.rmtree_error)
#             except PermissionError:
#                 mw.msg_one_button("Delete error", "Some files and folders were not deleted. "
#                                                   "Please do it manually", "info")
#         else:
#             try:
#                 _.unlink()
#             except PermissionError:
#                 os.chmod(_, stat.S_IWRITE)
#                 os.unlink(_)

