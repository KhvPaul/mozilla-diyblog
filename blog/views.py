from blog.models import Blog, Blogger, Comment

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .forms import AddCommentModelForm, CreateBloggerForm


def index(request):
    num_blogs = Blog.objects.count()
    num_authors = Blogger.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_blogs': num_blogs, 'num_authors': num_authors,
                 'num_visits': num_visits},
    )


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog

    def blog_detail_view(self, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(
            self,
            'blog/blog_detail.html',
            context={'blog': blog, }
        )


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    model = Blogger

    def blogger_detail_view(self, pk):
        blogger = get_object_or_404(Blogger, pk=pk)
        return render(
            self,
            'blog/blogger_detail.html',
            context={'blogger': blogger, }
        )


@login_required
def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blogger = get_object_or_404(Blogger, pk=request.user.blogger.id)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddCommentModelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            content = form.cleaned_data['content']
            comment = Comment(author=blogger, content=content, blog=blog)
            comment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('blog-detail', args=(pk,)))
    # If this is a GET (or any other method) create the default form.
    else:
        form = AddCommentModelForm()

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/comment_form.html', context)


def create_blogger(request):
    if request.method == 'POST':
        form = CreateBloggerForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            user.save()
            blogger = Blogger(user=user, bio=form.cleaned_data['bio'])
            blogger.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('login',) + f'?next={request.GET["next"]}')
    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateBloggerForm()

    context = {
        'form': form,
        'next': request.GET['next']
    }

    return render(request, 'blog/blogger_form.html', context)
