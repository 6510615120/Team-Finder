# Generated by Django 5.1.3 on 2024-11-22 23:54

import django.db.models.deletion
import django.utils.timezone
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('faculty', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('major', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('finish', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_tag', to='teamfinder_app.faculty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('communication_pt', models.IntegerField()),
                ('collaboration_pt', models.IntegerField()),
                ('reliability_pt', models.IntegerField()),
                ('technical_pt', models.IntegerField()),
                ('empathy_pt', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_feedbacks', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_feedbacks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamfinder_app.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MajorTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_tag', to='teamfinder_app.major')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecruitPost',
            fields=[
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teamfinder_app.post')),
                ('status', models.BooleanField(default=True)),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('post_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('reaction', models.CharField(blank=True, max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='teamfinder_app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('require_id', models.AutoField(primary_key=True, serialize=False)),
                ('year_min', models.IntegerField(default=1)),
                ('year_max', models.IntegerField(default=4)),
                ('description', models.TextField()),
                ('req_faculty', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='teamfinder_app.FacultyTag', to='teamfinder_app.Faculty', verbose_name='Tags')),
                ('req_major', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='teamfinder_app.MajorTag', to='teamfinder_app.Major', verbose_name='Tags')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='teamfinder_app.recruitpost')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='teamfinder_app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamfinder_app.requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('recruit_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teamfinder_app.post')),
                ('team_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='led_teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamfinder_app.team')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='fallback.png', null=True, upload_to='images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teamfinder_app.message')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_direct_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teamfinder_app.message')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_messages', to='teamfinder_app.group')),
            ],
        ),
        migrations.CreateModel(
            name='ResultPost',
            fields=[
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teamfinder_app.post')),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
