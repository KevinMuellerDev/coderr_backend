from rest_framework import serializers
from review_app.models import Review

class ReviewsSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['reviewer'] = user
        review = Review.objects.create(**validated_data)

        return review