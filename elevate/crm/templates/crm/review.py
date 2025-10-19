{% extends 'crm/base.html' %}

{% block content %}
<div class="container mt-4">

    <!-- 🔍 Search & ➕ Add Button -->
    <div class="d-flex justify-content-between align-items-center mb-3">
        <form method="GET" class="d-flex" style="width: 300px;">
            <input type="text" name="search" class="form-control" placeholder="Search reviews..." value="{{ request.GET.search }}">
            <button class="btn btn-primary ms-2">Search</button>
        </form>
        {% comment %} <a href="{% url 'add_review' %}" class="btn btn-success">+ Add New Review</a> {% endcomment %}
    </div>

    <h2 class="text-primary mb-3">Task Reviews</h2>
    <hr>

    {% for review in allReviews %}
        <div class="card mb-3 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">{{ review.review_title }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">
                    Reviewed by: <strong>{{ review.reviewer_name }}</strong>
                </h6>
                <p class="card-text">
                    <strong>Task:</strong> {{ review.task }}
                </p>

                <!-- 🛠 Actions -->
                {% comment %} <div class="mt-2">
                    <a href="{% url 'edit_review' review.id %}" class="btn btn-sm btn-warning">Edit</a>
                    <a href="{% url 'delete_review' review.id %}" class="btn btn-sm btn-danger"
                       onclick="return confirm('Are you sure?');">Delete</a>
                </div> {% endcomment %}
            </div>
        </div>
    {% empty %}
        <div class="alert alert-info">No reviews found.</div>
    {% endfor %}

    <!-- 📄 Pagination -->
    <div class="d-flex justify-content-center mt-4">
        {% if allReviews.has_previous %}
            <a class="btn btn-outline-primary mx-1" href="?page={{ allReviews.previous_page_number }}">Previous</a>
        {% endif %}

        <span class="btn btn-secondary disabled mx-1">Page {{ allReviews.number }} of {{ allReviews.paginator.num_pages }}</span>

        {% if allReviews.has_next %}
            <a class="btn btn-outline-primary mx-1" href="?page={{ allReviews.next_page_number }}">Next</a>
        {% endif %}
    </div>

</div>
{% endblock %}
