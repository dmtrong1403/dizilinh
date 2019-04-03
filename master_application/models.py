from django.db import models
from froala_editor.fields import FroalaField

from .global_variables import CATE_TYPE


#
# Category models
#

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    cate_type = models.CharField(max_length=2, choices=CATE_TYPE, verbose_name="Loại danh mục")
    description = FroalaField(default="",verbose_name="Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh đại diện")
    image_title = models.SlugField(max_length=100, verbose_name="Tiêu đề ảnh đại diện", default="")
    image_alt = models.SlugField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    is_homepage_content = models.BooleanField("Hiển thị ở trang chủ ?", default=True)
    code = models.SlugField(max_length=100, verbose_name="Đường dẫn danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 1"
        verbose_name_plural = "Danh mục cấp 1"

    def __str__(self):
        return str(self.name)


class DetailSubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = FroalaField(default="",verbose_name="Mô tả")
    image = models.ImageField(upload_to='category_images', verbose_name="Hình ảnh đại diện")
    image_title = models.SlugField(max_length=100, verbose_name="Tiêu đề ảnh đại diện", default="")
    image_alt = models.SlugField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    parent_cate = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="Danh mục cha")
    code = models.SlugField(max_length=100, verbose_name="Đường dẫn danh mục")

    class Meta:
        verbose_name = "Danh mục cấp 2"
        verbose_name_plural = "Danh mục cấp 2"

    def __str__(self):
        return str(self.name)


#
# Tag models
#

class PostTag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên tag")
    path = models.CharField(max_length=100, verbose_name="Đường dẫn", default="/bai-viet/")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"

    def __str__(self):
        return str(self.name)


class ProductTag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên tag")
    path = models.CharField(max_length=100, verbose_name="Đường dẫn", default="/san-pham/")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"

    def __str__(self):
        return str(self.name)


#
# Post models
#

class DetailPost(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên bài viết")
    avatar = models.ImageField(upload_to='post_avatar_images', verbose_name="Ảnh đại diện")
    image_title = models.SlugField(max_length=100, verbose_name="Tiêu đề ảnh đại diện", default="")
    image_alt = models.SlugField(max_length=100, verbose_name="Mô tả ảnh đại diện", default="")
    category = models.ForeignKey(DetailSubCategory, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="Danh mục")
    tag = models.ManyToManyField(PostTag, verbose_name="Tags")
    description = FroalaField(default="", verbose_name="Mô tả ngắn")
    code = models.SlugField(max_length=100, verbose_name="Đường dẫn bài viết")
    is_outstanding = models.BooleanField(default=False, verbose_name="Bài viết nổi bật ?")
    main_content = FroalaField(verbose_name="Nội dung chính", default="")

    class Meta:
        verbose_name = "Bài viết chi tiết"
        verbose_name_plural = "Bài viết chi tiết"

    def __str__(self):
        return str(self.name)

#
# Product models
#
